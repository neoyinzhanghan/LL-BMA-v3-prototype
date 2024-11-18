import os
from LLRunner.slide_processing.dzsave_h5 import dzsave_h5
from tqdm import tqdm

# this is a folder of ndpi files
ndpi_dir = "/media/hdd3/neo/error_slides_ndpi"
# this is a folder to save all the dzsave h5 files
save_dir = "/media/hdd3/neo/error_slides_h5"

os.makedirs(save_dir, exist_ok=True)

ndpi_files = [f for f in os.listdir(ndpi_dir) if f.endswith('.ndpi')]

for ndpi_file in tqdm(ndpi_files, desc='Converting ndpi to h5'):    
    ndpi_path = os.path.join(ndpi_dir, ndpi_file)
    h5_path = os.path.join(save_dir, ndpi_file.replace('.ndpi', '.h5'))

    dzsave_h5(
        wsi_path=ndpi_path,
        h5_path=h5_path,
        tile_size=512,
        num_cpus=32,
        region_cropping_batch_size=256,
    )