#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def calc_mean(numbers):
    return sum(numbers) / len(numbers) if numbers else 0

def calc_variance(numbers, mean):
    return sum((x - mean) ** 2 for x in numbers) / len(numbers) if numbers else 0

def calc_stan_dev(variance):
    return variance ** 0.5

def calc_stan_error(stan_dev, n):
    return stan_dev / (n ** 0.5) if n > 0 else 0

def calc_z(new_num, mean, stan_dev):
    return (new_num - mean) / stan_dev if stan_dev != 0 else 0


