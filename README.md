# ansible-role-nfs

CentOS 7 に nfs を導入する ansible role です。

## 設定項目

以下の設定項目は上書き可能。

| 項目名           | デフォルト値  | 説明                               |
| ---------------- | ------------- | ---------------------------------- |
| nfs_servier_mode | no            | nfs サーバモードで導入             |
| nfs_exports_path | /exports/data | サーバの export ディレクトリ（複数可） |
| nfs_exports_list | { path: '/exports/data', ipaddr: '127.0.0.1' } | サーバの export リスト（複数可） |
| nfs_mount_path   | /mnt/data     | クライアントのマウントディレクトリ |
| nfs_mount_list   | { path: '/mnt/data', src: '127.0.0.1:/exports/data' } | クライアントのマウントリスト（複数可） |
