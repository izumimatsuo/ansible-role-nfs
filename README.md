# ansible-role-nfs [![Build Status](https://travis-ci.org/izumimatsuo/ansible-role-nfs.svg?branch=master)](https://travis-ci.org/izumimatsuo/ansible-role-nfs)

CentOS 7 に nfs を導入する ansible role です。

## 設定項目

以下の設定項目は上書き可能。

| 項目名           | デフォルト値  | 説明                               |
| ---------------- | ------------- | ---------------------------------- |
| nfs_server_mode  | no            | nfs サーバモードで導入             |
| nfs_exports_path | /exports/data | サーバの exports ディレクトリ（複数可） |
| nfs_exports_list | { path: '/exports/data', ipaddr: '127.0.0.1' } | サーバの exports リスト（複数可） |
| nfs_mount_path   | /mnt/data     | クライアントの mount ディレクトリ（複数可） |
| nfs_mount_list   | { path: '/mnt/data', src: '127.0.0.1:/exports/data' } | クライアントの mount リスト（複数可） |
