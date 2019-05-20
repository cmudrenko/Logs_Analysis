#!/usr/bin/env python
import psycopg2

"""Udacity Logs Analysis project - database connections and queries"""
__author__ = "Chris Mudrenko"
__email__ = "cmudrenk@asu.edu"

NEWSDB = "news"

""" This function gives access to the news database"""


def connectQuery(news_query):
        try:
            newsdb = psycopg2.connect('dbname=' + NEWSDB)
            cursor = newsdb.cursor()
            cursor.execute(news_query)
            rows = cursor.fetchall()
            newsdb.close()
        return rows
        except Exception as e:
            print("Sorry there was an unexpected complication")

"""This function provides the top 3 most read articles"""


def getTopArticle():
    # Building the top articles string from database
    news_query = """
        select title, count(*) AS num
          from log join articles
          on log.path like '%' || articles.slug
          group by articles.title
          order by num desc
          limit 3;
    """

    # Connecting with query to get results from database
    topArticlesOutcome = connectQuery(news_query)

    # Formatting and printing outcome of database information
    print('\nTop Three Articles By Page Views:')
    print('------------------------------------\n')
    index = 1
    for i in topArticlesOutcome:
        print(str(index) + '. "' + i[0] + '" has ' + str(i[1]) + " views")
        index += 1

"""This function provides the top 3 top authors per their popularity"""


def getTopAuthors():

    # Building a query of the top authors per their popularity
    news_query = """
        select authors.name, count(*) as sum
          from authors join articles
          on authors.id = articles.author join log
          on log.path like '%' || articles.slug
          group by authors.name
          order by sum desc
          limit 3;
    """
    # Connecting with query to get results from database
    topAuthors = connectQuery(news_query)

    # Formatting and printing outcome of database information
    print('\nTop Three Authors By Views:')
    print('------------------------------\n')
    index = 1
    for i in topAuthors:
        print(str(index) + '. ' + i[0] + ' has ' + str(i[1]) + " views")
        index += 1

"""This function provides a list  of the days with more than 1% errors"""


def getDaysWithErrors():

    # Build Query with the days that had more than a 1% of error
    news_query = """
        select * from (select date(time),round(100.0*sum(case log.status
          when '200 OK' then 0 else 1 end)/count(log.status),3)
          as error from log group
          by date(time)
          order by error desc)
          as subq where error > 1;
    """

    # Connecting with query to get results from database
    results = connectQuery(news_query)

    # Formatting and printing outcome of database information
    print('\nDays With More Than 1% Errors:')
    print('--------------------------------\n')

    index = 1
    for i in results:
        print(
            str(index)+'. '+i[0].strftime('%B %d, %Y')+"--" +
            str(round(i[1], 1))+"%"+"errors\n")
        index += 1

# This will capture the three generated queries

print('Analyzing News Database for views comparisons and error calculation...')
getTopArticle()
getTopAuthors()
getDaysWithErrors()

