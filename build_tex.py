#!/usr/bin/python3

import os
import argparse
import glob
import shutil
import subprocess
import pathlib

class TexBuilder:
    def __init__(self, tex_relpath:str, src_dir:str=None, build_dir:str=None):
        self.inter_file_ext_white_list = ['tex', 'pdf']

        if src_dir is None:
            self.src_dir = os.path.join(os.path.dirname(__file__), 'src')
        else:
            self.src_dir = src_dir
        self.src_img_dir = os.path.join(self.src_dir, 'img')

        if build_dir is None:
            self.build_dir = os.path.join(os.path.dirname(__file__), 'build')
        else:
            self.src_dir = src_dir
        self.build_img_dir = os.path.join(self.build_dir, 'img')

        # print(self.src_dir)
        # print(self.build_dir)

        self.texname = os.path.splitext(os.path.basename(tex_relpath))[0]
        self.tex = os.path.join(self.build_dir, tex_relpath)


    def make_build_directory(self):
        os.makedirs(self.build_img_dir, exist_ok=True)


    def copy_images(self):
        src_image_paths = glob.glob(os.path.join(self.src_img_dir, '*'))
        for src_i in src_image_paths:
            i_name, i_ext = os.path.splitext(os.path.basename(src_i))
            i_eps = os.path.extsep.join([i_name, 'eps'])

            build_i_eps = os.path.join(self.build_img_dir, i_eps)

            src_i_timestamp = os.path.getmtime(src_i)

            if i_ext.replace(os.extsep, '').lower() == 'eps':
                if not os.path.exists(build_i_eps):
                    # shutil.copy(src_i, build_i_eps)
                    os.symlink(src_i, build_i_eps)
            else:
                if (not os.path.exists(build_i_eps)) or (os.path.getmtime(build_i_eps) < src_i_timestamp):
                    print('convert image | {} -> {}'.format(src_i, build_i_eps))
                    subprocess.run(['convert', src_i, 'eps2:' + build_i_eps], cwd=self.build_dir)
            # if (not os.path.exists(build_i_xbb)) or (os.path.getmtime(build_i_xbb) < src_i_timestamp):
            #     p = pathlib.Path(build_i_pdf).relative_to(build_dir)
            #     subprocess.run(['extractbb', p], cwd=self.build_dir)


    def symlink_otherfiles(self):
        src_paths = glob.glob(os.path.join(self.src_dir, '**'), recursive=True)
        for src_path in src_paths:
            if not os.path.isdir(src_path):
                dir = os.path.dirname(src_path)
                if not dir == self.src_img_dir:
                    os.makedirs(dir, exist_ok=True)

                    dst_path = src_path.replace(self.src_dir, self.build_dir, 1)
                    # if  (not os.path.exists(dst_path)) or \
                    #     (os.path.getmtime(dst_path) < os.path.getmtime(src_path)):
                    #     shutil.copy(src_path, dst_path)
                    if not os.path.exists(dst_path):
                        print('make symbolic link | {} -> {}'.format(src_path, dst_path))
                        os.symlink(src_path, dst_path)


    def tex2dvi(self):
        subprocess.run(['platex', self.tex], cwd=self.build_dir)


    def dvi2pdf(self):
        name, _ = os.path.splitext(self.tex)
        dvi = os.path.extsep.join([name, 'dvi'])
        subprocess.run(['dvipdfmx', dvi], cwd=self.build_dir)

    
    def remove_intermediate_files(self):
        paths = glob.glob(os.path.join(self.build_dir, '*'))
        for path in paths:
            _, ext = os.path.splitext(path)
            ext = ext.replace(os.extsep, '').lower()
            if (not os.path.isdir(path)) and (not ext in self.inter_file_ext_white_list):
                os.remove(path)




if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('texname', help='relative path from src_dir')
    parser.add_argument('--srcdir', type=str)
    parser.add_argument('--builddir', type=str)
    parser.add_argument('--hard', action='store_true')
    args = parser.parse_args()

    if 'srcdir' in args:
        src_dir = args.srcdir
    else:
        src_dir = None

    if 'builddir' in args:
        build_dir = args.builddir
    else:
        build_dir = None

    b = TexBuilder(args.texname, src_dir=src_dir, build_dir=build_dir)

    b.make_build_directory()
    b.copy_images()
    b.symlink_otherfiles()
    if args.hard:
        b.remove_intermediate_files()
        b.tex2dvi()
    b.tex2dvi()
    b.dvi2pdf()
