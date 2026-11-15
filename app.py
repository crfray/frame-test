"""Serve the static Frame demo using only Python's standard library."""
import argparse
import os
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--host', default='0.0.0.0')
    parser.add_argument('--port', type=int, default=int(os.environ.get('PORT', '8000')))
    args = parser.parse_args()
    directory = Path(__file__).resolve().parent / 'static'
    handler = partial(SimpleHTTPRequestHandler, directory=str(directory))
    with ThreadingHTTPServer((args.host, args.port), handler) as server:
        print('Frame: http://localhost:{}/ (Ctrl+C to stop)'.format(args.port), flush=True)
        try:
            server.serve_forever()
        except KeyboardInterrupt:
            print('\nServer stopped.', flush=True)


if __name__ == '__main__':
    main()
