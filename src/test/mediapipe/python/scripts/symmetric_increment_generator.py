#*****************************************************************************
# Copyright 2023 Intel Corporation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#*****************************************************************************
import numpy as np
from pyovms import Tensor
class OvmsPythonModel:

    def initialize(self, kwargs: dict):
        self.model_outputs = kwargs 
        return True

    def execute(self, inputs: list, kwargs: dict = {}):
        # Increment every element of every input and return them with changed tensor name.
        outputs = []
        inputs_npy = [np.array(input) for input in inputs]
        for _ in range(3):
            outputs = []
            for input_npy in inputs_npy:
                input_npy = input_npy + 1
                output_name = input.name.replace("INPUT", "OUTPUT")
                outputs.append(Tensor(output_name, input_npy))
            yield outputs

    def finalize(self, kwargs: dict):
        return None