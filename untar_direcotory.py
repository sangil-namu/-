#Search to .tar files. run to un tar
# windows


import tarfile, gzip
import requests, os, io, sys, time, csv, json, datetime
import pandas as pd

twodaysago = datetime.datetime.now() - datetime.timedelta(days=3)
twoym = twodaysago.strftime('%Y-%m')
twoymd = twodaysago.strftime('%Y%m%d')
nowtime = twodaysago.strftime('%Y%m%d')


temp_folder = r'd:\temp'
if not os.path.exists(temp_folder):
    os.mkdir(temp_folder)
   
folder = r'D:\folder'

def search(dirname):
    try:
        filenames = os.listdir(dirname)
        for filename in filenames:
            full_filename = os.path.join(dirname, filename)
            if os.path.isdir(full_filename):
                search(full_filename)
            else:
                ext = os.path.splitext(full_filename)[-1]
                if ext == '.tar': 
                    filedatea = full_filename.split('.')[4]
                    filedateb = filedatea[:8]
                    if filedateb == twoymd:   #search file name = 20180702 
                        with tarfile.open(full_filename, mode='r:') as tfile:
                            for gfile in tfile.getmembers():
                                gfile = gfile.name
                                if 'stat' in gfile: # search file name = stat
                                    temp_f = tfile.extract(gfile, path=temp_folder)

    except PermissionError:
        pass
search(folder)
