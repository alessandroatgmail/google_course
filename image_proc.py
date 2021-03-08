import PIL
import os

class process_imgs:

    def __init__(self, source_dir, dest_dir):
        if os.path.isdir(source_dir):
            self.source = source_dir
            self.dest = dest_dir
            self.status = 0
        else:
            self.status = -1
            self.err_msg = "Source directory does not exists"
            print (self.err_msg)




    # def load_imgs(self, source_dict):
    #
    # pass
    #
    # def transform_imgs
