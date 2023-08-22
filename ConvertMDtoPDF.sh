#!/bin/bash
ls *.md |  { 
    
    while read file;
    # for file in $files ;
        do 
            md2pdf $file $file".pdf" ;
    done;

    }