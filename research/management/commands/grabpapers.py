# -*- coding:utf-8 -*-
import os
import requests
import arxiv

from datetime import datetime, timedelta

from django.core.management.base import BaseCommand, CommandError

from research.models import *
#from utils import *

class Command(BaseCommand):
    help = 'Grab all interesting papers from arXiv.org'
    
    def get_authors(self, authors, first_author = False):
        output = str()
        if first_author == False:
            output = ", ".join(str(author) for author in authors)
        else:
            output = authors[0]
        return output
    
    def handle(self, *args, **kwargs):
        
        subjects = Subject.objects.all()

        for s in subjects:
            search = arxiv.Search(
              query = s.keywords,
              max_results = 10,
              sort_by = arxiv.SortCriterion.Relevance,
              sort_order = arxiv.SortOrder.Descending
            )
            
            for p in search.results():
                paper, _ = Paper.objects.get_or_create(short_id=p.get_short_id())
                paper.subject = s
                paper.title = p.title
                paper.summary = p.summary
                paper.published_date = p.published
                paper.updated_date = p.updated
                paper.authors = self.get_authors(p.authors)
                paper.save()