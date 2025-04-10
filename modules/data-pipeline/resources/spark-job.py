#!/usr/bin/env python
# Copyright 2018 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from __future__ import print_function
import tempfile
from pyspark.sql import SparkSession

# change to your data bucket
# DATA_BUCKET = "gs://tbd-2025l-9900-data/data/shakespeare/"
DATA_BUCKET = "gs://tbd-2025l-310269-data/data/weather/"

spark = SparkSession.builder.appName('Weather Rainfall Sort').getOrCreate()

table = 'bigquery-public-data.samples.weather'

df = spark.read.format('bigquery').load(table)
# Only these columns will be read
df = df.select('Rainfall')
# The filters that are allowed will be automatically pushed down.
df = df.orderBy(df['Rainfall'].desc()).cache()

print('The resulting schema is')
df.printSchema()

print('Rainfall sorted is')
df.show()
df.write.mode("overwrite").orc(DATA_BUCKET)

spark.stop()