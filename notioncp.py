import argparse
import notion_client as nc
import sys
from datetime import datetime
try:
  import env
except ImportError:
  env = None

def main(arglist):
  parser = argparse.ArgumentParser(
    prog='notioncp',
    description=(
      'Internal utility for Yonder Dynamics Science Lab subteam to '
      'upload test result CSVs to Notion.'
    ),
  )
  parser.add_argument(
    '--token-file',
    required=env is None,
    help=(
      f'{"Required because %(prog)s was packaged without an API key. " if env is None else ""}'
      'The path to a file containing the Notion API key.'
    )
  )
  parser.add_argument(
    '--date',
    metavar='MM-DD-YYYY',
    type=lambda s: datetime.strptime(s, '%m-%d-%Y'),
    help=(
      'If given, overrides the timestamp the uploaded CSVs are marked with. '
      'Otherwise, uses the current date.'
    ),
    default=datetime.now(),
  )
  parser.add_argument(
    '--test',
    required=True,
    choices=('raman', 'nile-red', 'ninhydrin'),
    help='The assay the uploaded test results are for.',
  )
  parser.add_argument(
    'csvs',
    help='The result CSVs to upload to Notion.',
  )
  args = parser.parse_args(arglist)

  # TODO: actual notion api stuff :)

if __name__ == '__main__':
  main(sys.argv[1:])
