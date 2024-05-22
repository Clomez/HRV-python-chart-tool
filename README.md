# HRV-python-chart-tool
Script to draw charts from Polar HRV data
Requirements:
- Python
- Polar Night data (Nightly_recovery_xxx..xx.json)

Usage:
1. Run cli command - this will take the raw json data and put it into a new file
> ./parse.sh

OR
otherwise run cli command to parse the data:
> cat night.json | jq '[.[] | .hrvData[] | {startTime, avg: (.samples | add / length), median: (.samples | sort | if length % 2 == 0 then ((.[length / 2 - 1] + .[length / 2]) / 2) else .[length / 2] end)}]' > stats.json
2. when data json is parsed properly then run
> py draw.py

![c4b26fb6430e1c947dac3a825eef27cbab9c387c6d273c2ee14ee5734247b8dd](https://github.com/Clomez/HRV-python-chart-tool/assets/17356557/b6091590-ada7-4b81-8ecc-3dd4eafa1b8e)


Example parsed data:
```
  {
    "startTime": "2024-04-22T05:45:46",
    "avg": 58.42373070863114,
    "median": 59.83704229994723
  },
  {
    "startTime": "2024-04-22T22:17:57",
    .....
    "avg": 55.33175447137666,
    "median": 56.97143460456526
  },
```

  Example unparsed data:
```
{
    "hrvData": [
      {
        "startTime": "2023-06-28T01:12:51",
        "samplingIntervalInMillis": 301000,
        "samples": [
          14.14567935797986,
          16.793304480562615,
          24.94875577073478,
          21.25612346619502,
          20.373567733973275,
          ...
```
