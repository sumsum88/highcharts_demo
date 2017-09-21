#!/usr/bin/env python # coding: utf-8

def format_for_highcharts(df):
    """
    see https://www.highcharts.com/demo
    :param df: pd.DataFrame
    :return:
    """
    df.index = list(df.index.fillna('NODATA'))
    categories = list(df.columns.fillna('NODATA'))

    df = df.fillna(0)
    series = [{'name': index, 'data': list(map(int, row))} for index, row in df.iterrows()]
    return {'categories': categories, 'series': series}