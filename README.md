# dataflow-demo
A demo project for data services using thrift.

## Installation
Clone dataflow-demo project from github.
```bash
git clone https://github.com/lixx11/dataflow-demo.git
```

Install [Anaconda](https://www.anaconda.com/distribution/).

Install dependencies.
```bash
pip install -r requirements.txt
```

Install dataflow_demo
```bash
python setup.py install
```

All done!

## Test
```
python -m dataflow_demo.clients.data_api 121.89.209.254 10000
python -m dataflow_demo.clients.signal_api 121.89.209.254 10001
```
