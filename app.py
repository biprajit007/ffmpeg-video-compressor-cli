#!/usr/bin/env python3
"""Compress videos with CRF, preset, and scaling options."""
import argparse, shutil, subprocess

def require(x):
    if shutil.which(x) is None: raise SystemExit(f'Missing required binary: {x}')

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('input'); p.add_argument('output'); p.add_argument('--crf',type=int,default=23); p.add_argument('--preset',default='medium'); p.add_argument('--scale'); p.add_argument('--dry-run',action='store_true')
    a=p.parse_args(); require('ffmpeg')
    cmd=['ffmpeg','-y','-i',a.input]
    if a.scale: cmd += ['-vf',f'scale={a.scale}']
    cmd += ['-c:v','libx264','-preset',a.preset,'-crf',str(a.crf),'-c:a','aac','-b:a','128k',a.output]
    print(' '.join(cmd))
    if not a.dry_run: subprocess.check_call(cmd)
if __name__ == '__main__': main()
