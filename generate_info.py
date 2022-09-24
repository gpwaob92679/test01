import argparse
import json

CLOCK_SVG = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" fill="#fff"><!--! Font Awesome Pro 6.2.0 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license (Commercial License) Copyright 2022 Fonticons, Inc. --><path d="M232 120C232 106.7 242.7 96 256 96C269.3 96 280 106.7 280 120V243.2L365.3 300C376.3 307.4 379.3 322.3 371.1 333.3C364.6 344.3 349.7 347.3 338.7 339.1L242.7 275.1C236 271.5 232 264 232 255.1L232 120zM256 0C397.4 0 512 114.6 512 256C512 397.4 397.4 512 256 512C114.6 512 0 397.4 0 256C0 114.6 114.6 0 256 0zM48 256C48 370.9 141.1 464 256 464C370.9 464 464 370.9 464 256C464 141.1 370.9 48 256 48C141.1 48 48 141.1 48 256z"/></svg>'
DIFF_SVG = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="24" height="24" fill="#fff"><path d="M12.5 6.75a.75.75 0 00-1.5 0V9H8.75a.75.75 0 000 1.5H11v2.25a.75.75 0 001.5 0V10.5h2.25a.75.75 0 000-1.5H12.5V6.75zM8.75 16a.75.75 0 000 1.5h6a.75.75 0 000-1.5h-6z"></path><path fill-rule="evenodd" d="M5 1a2 2 0 00-2 2v18a2 2 0 002 2h14a2 2 0 002-2V7.018a2 2 0 00-.586-1.414l-4.018-4.018A2 2 0 0014.982 1H5zm-.5 2a.5.5 0 01.5-.5h9.982a.5.5 0 01.354.146l4.018 4.018a.5.5 0 01.146.354V21a.5.5 0 01-.5.5H5a.5.5 0 01-.5-.5V3z"></path></svg>'


def dump_timestamp(args) -> None:
    timestamp_dict = {
        'schemaVersion': 1,
        'label': 'Timestamp',
        'message': args.timestamp,
        'color': 'informational',
        'logoSvg': CLOCK_SVG,
        'style': 'flat',
        'cacheSeconds': 300,
    }
    with open('timestamp.json', 'w', encoding='utf-8') as f:
        json.dump(timestamp_dict, f, indent=2)


def dump_changes(args) -> None:
    changes_dict = {
        'schemaVersion': 1,
        'label': 'Changes since last clone',
        'message': 'Yes' if args.changes else 'No',
        'color': 'orange' if args.changes else 'lightgrey',
        'logoSvg': DIFF_SVG,
        'style': 'flat',
        'cacheSeconds': 300,
    }
    with open('changes.json', 'w', encoding='utf-8') as f:
        json.dump(changes_dict, f, indent=2)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('timestamp', type=str)
    parser.add_argument('-c', '--changes', action='store_true')
    args = parser.parse_args()
    print(args)

    dump_timestamp(args)
    dump_changes(args)


if __name__ == '__main__':
    main()
