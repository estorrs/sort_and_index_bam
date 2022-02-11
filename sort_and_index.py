import argparse
import logging
import subprocess
from pathlib import Path

logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)

parser = argparse.ArgumentParser()

parser.add_argument('input_bam', type=str,
    help='input bam')

parser.add_argument('output_bam', type=str,
    help='output bam filepath')

parser.add_argument('--cpu', type=int, default=1,
    help='threads to use while sorting')


args = parser.parse_args()


def sort_bam(input_bam, output_bam, cpu):
    pieces = [
        'samtools sort',
        input_bam,
        '-o', output_bam,
        '-@', str(cpu),
    ]
    return ' '.join(pieces)


def index_bam(bam):
    pieces = [
        'samtools index',
        bam,
    ]
    return ' '.join(pieces)


def run(input_bam, output_bam, cpu):
    logging.info('sorting input bam')
    cmd = sort_bam(input_bam, output_bam, cpu)
    logging.info(f'executing command: {cmd}')
    subprocess.check_output(cmd, shell=True)

    logging.info('indexing bam')
    cmd = index_bam(output_bam)
    logging.info(f'executing command: {cmd}')
    subprocess.check_output(cmd, shell=True)


def main():
    Path(args.out_dir).mkdir(parents=True, exist_ok=True)
    run(args.input_bam, args.output_bam, args.cpu)


if __name__ == '__main__':
    main()
