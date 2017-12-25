#!/bin/sh

yum install -y https://ecsft.cern.ch/dist/cvmfs/cvmfs-release/cvmfs-release-latest.noarch.rpm
yum install -y cvmfs cvmfs-config-default
rpm -ivh http://cvmfs-stratum-one.ihep.ac.cn/cvmfs/software/cvmfs-config-ihep-1.3-1.noarch.rpm

cat >/etc/cvmfs/default.local <<EOL
CVMFS_REPOSITORIES=cepc.ihep.ac.cn
CVMFS_CACHE_BASE=/var/lib/cvmfs
CVMFS_QUOTA_LIMIT=4096
CVMFS_HTTP_PROXY=DIRECT
EOL

echo 'Disable SELinux...'
setenforce 0
sed -i 's/SELINUX=enforcing/SELINUX=disabled/' /etc/sysconfig/selinux

cvmfs_config setup

service autofs restart

cvmfs_config chksetup
cvmfs_config probe

echo 'CVMFS installation finished'
