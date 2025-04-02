# Apr-02-2025
# main.py

import time
from pathlib import Path

from max3.src import cfg
from max3.src.utils import init_directory, remove_directory
from max3.src.get_shapes_distance import get_shapes_distance


# Input Data
# -------------------------------------------------------------
cfg.image_name = '4star_1.png'
cfg.templ_name = '4star_24.png'
# -------------------------------------------------------------

cfg.dir_data = 'IMAGES_DATA'
cfg.dir_debug = 'DEBUG'

cfg.path_image \
    = str(Path.cwd() / cfg.dir_data / cfg.image_name)
cfg.path_templ \
    = str(Path.cwd() / cfg.dir_data / cfg.templ_name)

if cfg.debug_mode:
    init_directory(cfg.dir_debug)
else:
    remove_directory(cfg.dir_debug)

begin = time.time()

distance = get_shapes_distance(cfg.path_image, cfg.path_templ)

end = time.time()

print(f'\n{cfg.image_name}  &  {cfg.templ_name}'
      f'\ndistance = {distance:.5f}'
      f'\ntime = {(end - begin):.1f} sec')
