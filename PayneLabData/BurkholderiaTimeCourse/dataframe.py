#   Copyright 2018 Samuel Payne sam_payne@byu.edu
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#       http://www.apache.org/licenses/LICENSE-2.0
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.

import numpy as np
import pandas as pd
import os
import re
from .fileLoader import FileLoader
class DataFrameLoader:
    def __init__(self, fileName):
        self.fileName = fileName
    def createDataFrame(self):
        """
        Parameters
        None

        Returns
        Dataframe of parsed datafile depending on the data type
        """
        if bool(re.search(r'\.xlsx[.|(a-z)]{,7}$', self.fileName)):
            df = pd.read_excel(self.fileName, index_col=0)
            df = df.sort_index()

            f = self.fileName.split(os.sep)
            f = f[len(f) - 1]
            df.name = f.split(".")[0]
            return df
        else:
            print("Error reading", self.fileName)
