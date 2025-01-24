
import logging
import os
from shutil import copy

from pysam import bedcov


def get_logger(name: str = "comebin"):
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    formatter = logging.Formatter('[ %(asctime)s ] - %(message)s')
    if not logger.handlers:
        console_hdr = logging.StreamHandler()
        console_hdr.setFormatter(formatter)
        logger.addHandler(console_hdr)
    return logger

# run_comebin.sh -a /home/datasets/ZOUbohao/Proj1-Deepurify/Data_marine/1021526/1021526.contigs.fasta 
# -o ../1021526-comebin-outputs -p /home/datasets/ZOUbohao/Proj1-Deepurify/Data_marine/1021526/ -t 32
if __name__ == "__main__":
    logger = get_logger()
    home_path = "/home/datasets/ZOUbohao/Proj3-DeepMetaBin/CAMI-Marine-contigs-bam-multi-samples"
    out_folder = "/home/datasets/ZOUbohao/Proj3-DeepMetaBin/Comebin-marine-multi-sample"
    if os.path.exists(out_folder) is False:
        os.mkdir(out_folder)
    
    for i in range(10):
        id_name = f"marine-sample-{i}"
        cur_sample_folder = os.path.join(home_path, id_name)
        if os.path.exists(cur_sample_folder) is False:
            os.mkdir(cur_sample_folder)
        logger.info(f"--> Start to copy bam file.")
        bam_list = []
        for j in range(10):
            print(j)
            bam_list.append(os.path.join(home_path, f"marine-sample-c{i}-r{j}.sorted.bam"))
            if os.path.exists(os.path.join(cur_sample_folder, f"marine-sample-c{i}-r{j}.sorted.bam")) is False:
                copy(
                    os.path.join(home_path, f"marine-sample-c{i}-r{j}.sorted.bam"),
                    cur_sample_folder
                )
        logger.info(f"--> Start to copy contig file.")
        copy(
            os.path.join(home_path, f"{id_name}.contigs.fasta"),
            cur_sample_folder
        )
        cmd = f"run_comebin.sh -a {os.path.join(cur_sample_folder, f'{id_name}.contigs.fasta')}" + \
            f" -o {os.path.join(out_folder, f'{id_name}-outputs')} -p {cur_sample_folder} -t 32"
        logger.info(cmd)
        os.system(cmd)


