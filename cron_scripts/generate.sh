#!/bin/sh

cd /opt/almanax && \
    python3 almanax_next_week.py public/index.html && \
    cd - &>/dev/null
