#!/usr/bin/bash

export PASSIVE="0"

exec ./launch_chffrplus.sh  &
exec ./eon-custom-themes/install_theme.py &

wait
echo all processes complete

