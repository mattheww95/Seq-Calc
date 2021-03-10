# crispy_cody
Calculate Breadth of coverage from either a directory of bam and bai files, or from a single bam and bai file.

FOR THE CODIES OUTTHERE:
  - git clone https://github.com/mattheww95/crispy_cody.git
  - cd into the folder
  - then create a conda environment conda create -n crispy_cody -f environment.yml


environment.yml file is included in the directory to create a conda envrionment. This script requires pysam, so it will only run on linux.
Eventually crispy cody will get crispier, by adding in the ability to add the depth of a given postion to a provided VCF


The help output is provided below, if there any questions please e-mail me. Similarly if you are Cody, just come ask me.

usage: crispy_cody.py 
[-h]

[-b BAM] 

[-i BAM_INDEX] 

[-t THRESHOLD]

[-d DIRECTORY_SCAN] 

[-v VERBOSE] 

[-l GENOME_LENGTH]

[-x LOG]

Calculate the breadth of coverage for a sequence

optional arguments:
  -h, --help            show this help message and exit
  
  -b BAM, --bam BAM     Specify input bam file
  
  -i BAM_INDEX, --bam_index BAM_INDEX
                        Index file for bam to be calculated
                        
  -t THRESHOLD, --threshold THRESHOLD
                        Set the threshold for the pileup coverage, default
                        value is 5
                        
  -d DIRECTORY_SCAN, --directory_scan DIRECTORY_SCAN
                        path to directory containing bams and bai files, files
                        must have shared handle before first '.' appears
                        
  -v VERBOSE, --verbose VERBOSE
                        Use a verbose output, default is False
                        
  -l GENOME_LENGTH, --genome_length GENOME_LENGTH
                        Length of genome to be calculated, default is 29903
                        
  -x LOG, --log LOG     Default is false, set to true to have output saved to
                        log file in thecurrent working directory. Default is
                        false, enter true for a log to be generated. A
                        previous log file will be over written if present.The
                        output location will be in the current directory
