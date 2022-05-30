## WhoaVH

Small utility to track expiring or active domains / VPS / Servers @ OVH.

Uses https://github.com/ovh/python-ovh

### Installation

1. `git clone https://github.com/jarviscodes/whoavh`
2. `pip3 install -r requirements.txt`

### Usage

Because you have to confirm authorization manually, currently still interactive-only scripting:

**iPython Example**

```
In [1]: from whoavh.connector import OVHAppConnector

In [2]: x = OVHAppConnector()

In [3]: x.get_consumer_key_token()
deadbeefdeadbeefdeadbeef781a6bda

In [4]: x.get_client_data()
{'corporationType': ... }

```



