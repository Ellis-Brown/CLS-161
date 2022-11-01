---
layout: page
title: Exercises Book contents to CSV
description: Transform the Odyssey from project gutenberg to csv format by paragraph
---


```python
import pandas as pd
file = open("../data/Odyssey", encoding="utf8")
file_data = file.readlines()
```


```python
# Take the lines, and turn it into a string for processing.
# We are looking for multiple \n in a row, which indicates a new paragraph
data = ""
for line in file_data:
    data += line
```


```python
# First, seperate the text into the data frame based on newline characters
paras = dict()
paragraphs = data.split("\n\n")

print(len(paragraphs))
labels = ["Paragraph " + str(index) for index in range(len(paragraphs))]
dataframe = pd.DataFrame(paragraphs, index = labels, columns = ["Chapter content"])

# dataframe.columns = ["Paragraph Label", "Paragraph Contents"]
dataframe.to_csv("odyssey_paragraphs.csv")
dataframe
```

    1106





<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Chapter content</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Paragraph 0</th>
      <td>INTRODUCTION.</td>
    </tr>
    <tr>
      <th>Paragraph 1</th>
      <td>\nIt is quite unnecessary here to discuss the ...</td>
    </tr>
    <tr>
      <th>Paragraph 2</th>
      <td>There is extant a Life of the poet, said to ha...</td>
    </tr>
    <tr>
      <th>Paragraph 3</th>
      <td>“Whom the Muse loved, and gave him good an...</td>
    </tr>
    <tr>
      <th>Paragraph 4</th>
      <td>So, in the same poem, the only other bard who ...</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
    </tr>
    <tr>
      <th>Paragraph 1101</th>
      <td>Professor Michael S. Hart is the originator of...</td>
    </tr>
    <tr>
      <th>Paragraph 1102</th>
      <td>\nProject Gutenberg-tm eBooks are often create...</td>
    </tr>
    <tr>
      <th>Paragraph 1103</th>
      <td>\nMost people start at our Web site which has ...</td>
    </tr>
    <tr>
      <th>Paragraph 1104</th>
      <td>http://www.gutenberg.org</td>
    </tr>
    <tr>
      <th>Paragraph 1105</th>
      <td>This Web site includes information about Proje...</td>
    </tr>
  </tbody>
</table>
<p>1106 rows × 1 columns</p>
</div>




```python
file.close()
```


```python

```


```python

```


```python

```
