# HW 12 IBM's General Parallel File System

### Questions

#### 1. 
Total disk space after running the crawlers for 24 hours:

```
[root@gpfs1 gpfsfpo]# du -h .
1.1G	./aus_gut_dataset
355M	./reddit_urls.dataset
1.9G	./reddit_urls
517M	./wikitext-103
15G	./us_gutenberg.dataset
512	./.snapshots
25G	.
```

#### 2. 
As a test for this assignment I ran three in parallel on a single virtual manchine as follows:

``` bash
time python3 crawler.py reddit_urls/RS_2011-01.bz2.deduped.2.txt reddit_urls.dataset > reddit_log1.txt &
time python3 crawler.py reddit_urls/RS_2011-01.bz2.deduped.txt reddit_urls.dataset > reddit_log2.txt &
time python3 crawler.py reddit_urls/RS_2011-02.bz2.deduped.txt reddit_urls.dataset > reddit_log3.txt &
```


I noticed that CPU usage for the crawlers was consistantly below 5%, so I would write a script that would call each of the reddit url files, in parallel, across the three nodes we setup. 


#### 3. 
In Step 2 of the Lazynlp crawler docs (https://github.com/chiphuyen/lazynlp) they outline how to de-duplicate the urls before download.  Since I ran each dataset to output to different folders, and the Reddit URLs were already deduplicated, I didn't need to run this step

#### Times:

```
Gutenberg AUS : 2 hrs, 8 minutes

Gutenberg US: 16 hrs, 38 minutes

Reddit URLs: stopped at 24 hrs
```
