#!/bin/bash

wget https://snap.stanford.edu/snappy/release/snap-3.0.2-3.0-centos6.5-x64-py2.6.tar.gz
tar -xzf snap-3.0.2-3.0-centos6.5-x64-py2.6.tar.gz snap-3.0.2-3.0-centos6.5-x64-py2.6/snap.py
tar -xzf snap-3.0.2-3.0-centos6.5-x64-py2.6.tar.gz snap-3.0.2-3.0-centos6.5-x64-py2.6/_snap.so
mv snap-3.0.2-3.0-centos6.5-x64-py2.6/snap.py .
mv snap-3.0.2-3.0-centos6.5-x64-py2.6/_snap.so .
rm -rf snap-3.0.2-3.0-centos6.5-x64-py2.6.tar.gz snap-3.0.2-3.0-centos6.5-x64-py2.6/