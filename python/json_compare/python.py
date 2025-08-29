import json
import argparse
import sys

def compare_json(obj1, obj2, prefix=""):
    diffs = []

    for key in obj1.keys() - obj2.keys():
        if key == "effectiveDate":
            continue
        diffs.append(f"Key only in File1: {prefix}{key}")

    for key in obj2.keys() - obj1.keys():
        if key == "effectiveDate":
            continue
        diffs.append(f"Key only in File2: {prefix}{key}")

    for key in obj1.keys() & obj2.keys():
        if key == "effectiveDate":
            continue
        v1 = obj1[key]
        v2 = obj2[key]
        current_prefix = f"{prefix}{key}."

        if isinstance(v1, dict) and isinstance(v2, dict):
            diffs += compare_json(v1, v2, prefix=current_prefix)
        elif isinstance(v1, list) and isinstance(v2, list):
            if len(v1) != len(v2):
                diffs.append(f"Different list lengths at {current_prefix} ({len(v1)} vs {len(v2)})")
            else:
                for i, (item1, item2) in enumerate(zip(v1, v2)):
                    list_prefix = f"{current_prefix}[{i}]."
                    if isinstance(item1, dict) and isinstance(item2, dict):
                        diffs += compare_json(item1, item2, prefix=list_prefix)
                    else:
                        if item1 != item2:
                            diffs.append(f"List difference at {current_prefix}[{i}]: File1={item1} | File2={item2}")
        else:
            if v1 != v2:
                diffs.append(f"Value difference at {current_prefix}: File1={v1} | File2={v2}")
    return diffs

def main(file1, file2, output_path=None):
    try:
        with open(file1, 'r') as f1, open(file2, 'r') as f2:
            data1 = json.load(f1)
            data2 = json.load(f2)
    except Exception as e:
        print(f"Error reading files: {e}")
        sys.exit(1)

    header = f"Comparing:\n  File1: {file1}\n  File2: {file2}\n"

    if isinstance(data1, dict) and isinstance(data2, dict):
        diffs = compare_json(data1, data2)
    else:
        diffs = ["Top-level objects are not both dicts, only shallow comparison done."]
        if data1 != data2:
            diffs.append(f"File1 top-level != File2 top-level: {data1} vs {data2}")

    if not diffs:
        result = header + "\nNo differences found."
        print(result)
        if output_path:
            with open(output_path, 'w') as out:
                out.write(result)
    else:
        if output_path:
            with open(output_path, 'w') as out:
                out.write(header)
                out.writelines(diff + '\n' for diff in diffs)
            print(f"Done. Differences written to {output_path}")
        else:
            print(header)
            print("Differences found:")
            for diff in diffs:
                print(diff)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Compare two JSON files.")
    parser.add_argument("file1", help="First JSON file path")
    parser.add_argument("file2", help="Second JSON file path")
    parser.add_argument("--output", "-o", dest="output_path", help="Output file to write results", default=None)
    args = parser.parse_args()

    main(args.file1, args.file2, output_path=args.output_path)
