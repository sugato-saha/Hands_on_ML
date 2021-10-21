from pathlib import Path 
import tarfile
from urllib import request

housing_url = "https://raw.githubusercontent.com/ageron/handson-ml2/master/datasets/housing/housing.tgz"
download_path = "C:/Users/Sugato/STUDIES/Hands_on_ML/datasets"

def fetch_housing_data() :
    housing_dir = Path(download_path) / "housing"
    housing_dir.mkdir(exist_ok=True)
    tgz_path = housing_dir / "housing.tgz"
    request.urlretrieve(housing_url,tgz_path)
    housing_tgz = tarfile.open(tgz_path)
    housing_tgz.extractall(path=housing_dir)
    housing_tgz.close()
    
# for testing purposes
# fetch_housing_data()



