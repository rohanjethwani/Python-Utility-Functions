import gzip
import os
import shutil
import zipfile
import contextlib

def createDir(dir):
    """
    This function creates a directory, if it does not exists. If dir exists, it does not do anything.
    """
    os.makedirs(dir, exist_ok=True)
    

def readFileCOntenrs(fileName):
    """
    This function opens file in read only mode and returns file contents as a list
    """    
    content = ([line.strip() for line in open(fileName, "r")])
    return content


def readFileContentsHavingString(fileName, str):
    """
    This function returns file contents as a list if str is present in the line. If file is not present, blank list will be returned.
    """
    content = []
    with open(fileName, "a+") as f:
        f.seek(0)
        for line in f:
            if str in line:
                content.append(line.strip())
        f.close()
    
    return content


def writeFileContents(fileName, content):
    """
    This function opens the file for reading and writing and overwrites file contents passed as a list
    """
    with open(fileName, "w+") as rows:
        rows.write("\n".join(content))
    rows.close()
    
    
def appendFileContents(fileName, content):
    """
    This function opens the file for reading and appending and appends file contents passed as a list
    """
    with open(fileName, "a+") as rows:
        rows.write(content + "\n")
    rows.close()
    
    
def compressFileInZip(file):
    """
    This function compress the file in zip format
    """
    with contextlib.closing(zipfile.ZipFile(file + '.zip', 'w', compression = zipfile.ZIP_DEFLATED, allowZip64 = True)) as zipped:
        zipped.write(file, os.path.basename(file))
    zipped.close()
    
    
def uncompressFileInZip(zippedFile, targetDir, **kwargs):
    """
    This function uncompresses ZIP file and places the unzipped file(s) in targetDir.
    It supports optional paramter "overwrite_filename". When passed, the extracted file name(s) is overwritten by this string followed by index.
    E.g. If zipped file contains ABC.txt, the extracted file will be ABC.txt (without optional parameter); NewFile_1.txt (with overwrite_filename as 'NewFile')
    """
    overwrite_filename = kwargs.get('overwrite_filename') 
    
    if not os.path.exists(targetDir):
        os.mkdir(targetDir)
        
    with zipfile.ZipFile(zippedFile, 'r') as zip_ref:
        file_infos = zip_ref.infolist()
        for file_info in file_infos:
            index = 1
            file_info_ext = os.path.splitext(file_info.filename)[1]
            file_info.filename = overwrite_filename = "_" + str(index) + file_info_ext if overwrite_filename else file_info.filename
            zip_ref.extract(file_info, targetDir)
            index += 1
    zip_ref.close()
    
    
def compressFileInGZ(fileName):
    """
    This function compresses file in .gz format
    """
    with gzip.open(fileName + '.gz', 'wt') as mygz:
        mygz.write(open(fileName).read())
    mygz.close()
    
    
def moveFile(sourceFile, destinationFile):
    """
    This function moves the file from source location to destination location. Absolute paths are expected in parameters.
    """
    destination_dir = os.path.dirname(destinationFile)
    if not os.path.exists(destination_dir):
        os.mkdir(destination_dir)
    shutil.move(sourceFile, destinationFile)
    
    
def silentDelete(fileName):
    """
    This function deletes a file, if it exists.
    """
    if os.path.exists(fileName):
        os.remove(fileName)
