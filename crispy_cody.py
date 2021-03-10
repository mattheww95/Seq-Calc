import pysam
import argparse
import sys
import os


def scan_dir(directory):
    bams = list(os.listdir(directory))
    bais = []
    bam = []
    combo = {}
    for i in bams:
        if i[-3:] == 'bam':
            bam.append(i)
        elif i[-3:] == 'bai':
            bais.append(i)
        else:
            continue
    for ii in bais:
        for iii in bam:
            if ii[0:ii.index('.')] == iii[0:iii.index('.')]:
                combo[iii] = ii
            else:
                continue
    return combo


def actual_calc(bam, bai, thresh):
    bamfile = bam
    bamindex = bai
    bamfile = pysam.AlignmentFile(bamfile, "rb")
    if args.verbose[0].upper() == 'T':
        print(bamfile.header)

    crispiest_cody = 0
    for pileupcolumn in bamfile.pileup(contig='MN908947.3', truncate=False, max_depth=10000, min_base_quality=1,
                                       filepath_index=bamindex):
        #  print("\ncoverage at base %s = %s" % (pileupcolumn.pos, pileupcolumn.n))
        if pileupcolumn.n < thresh:
            crispiest_cody += 1
    bamfile.close()
    b_cov = round((float(args.genome_length - crispiest_cody) / args.genome_length) * 100, 2)

    print('\n')
    print("THE BREADTH OF COVERAGE FOR SAMPLE {} IS {} %".format(bam, b_cov))
    print(f"THE TOTAL NUMBER OF N's FOUND IS {crispiest_cody}")
    print('\n'*4)


def check_scan_dir(dict_of_pairs, thresh):
    if dict_of_pairs is not None:
        print("directory scan chosen")
        for i in dict_of_pairs.keys():
            print("Sample being used", i, dict_of_pairs[i])
            actual_calc(bam=i, bai=dict_of_pairs[i], thresh=thresh)
        sys.exit("Finished")
    else:
        pass


def check_for_args(arg, success, scan):
    if arg is not None:
        return True
    elif scan is not None:
        pass
    else:
        parser.print_help()
        sys.exit(f"Missing required argument {success}")


def dir_path(string):
    if os.path.isdir(string):
        return string
    else:
        raise NotADirectoryError(string)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Calculate the breadth of coverage for a sequence')
    parser.add_argument('-b', '--bam', help='Specify input bam file', action='store')
    parser.add_argument('-i', '--bam_index', help='Index file for bam to be calculated', action='store')
    parser.add_argument('-t', '--threshold', help='Set the threshold for the pileup coverage, default value is 5',
                        type=int, default=5, action='store')
    parser.add_argument('-d', '--directory_scan', action='store',
                        help="path to directory containing bams and bai files, files must have shared handle "
                             "before first '.' appears", type=dir_path)
    parser.add_argument('-v', '--verbose', help='Use a verbose output, default is False',
                        action='store', default="FALSE")
    parser.add_argument('-l', '--genome_length', help="Length of genome to be calculated, default is 29903",
                        default=29903, type=int)
    parser.add_argument('-x', '--log', help="Default is false, set to true to have output saved to log file in the"
                                            "current working directory. Default is false, enter true for a log "
                                            "to be generated. A previous log file will be over written if present."
                                            "The output location will be in the current directory",
                        action='store', default='f')

    args = parser.parse_args()
    log = None
    if args.log[0].upper == 'T':
        log = open("Crispy_Codys_log.log", "w")
        sys.stdout = log

    bam_1 = check_for_args(arg=args.bam, success="Bam file", scan=args.directory_scan)
    bai_1 = check_for_args(arg=args.bam_index, success="Bam index", scan=args.directory_scan)
    threshold = args.threshold

    if bam_1 and bai_1:
        actual_calc(bam=args.bam, bai=args.bam_index, thresh=threshold)
    else:
        files = scan_dir(args.directory_scan)
        check_scan_dir(files, thresh=threshold)
        if args.log:
            log.close()

