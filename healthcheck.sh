#!/bin/bash
echo "========== SYSTEM HEALTH CHECK =========="
echo ""
echo "--- CPU & Memory ---"
free -h
echo ""
echo "--- Disk Space ---"
df -h
echo ""
echo "--- System Uptime ---"
uptime
echo ""
echo "--- Who is Logged In ---"
who
echo ""
echo "========== CHECK COMPLETE =========="
