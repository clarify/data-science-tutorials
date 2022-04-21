![Clarify Logo](https://global-uploads.webflow.com/5e81e464dad44d3a9a32d1f4/5ed10fc3f1ff8467f4466786_logo.svg)

# Clarify Data Science Tutorials

> _A space for data science tutorials using Clarify._

![doodle](media/light-3.png)

## Table of Contents

1. [Introduction](#intro)
2. [Forecasting](#forecasting)
3. [Pattern Recognition](#pattern)
4. [Google Cloud Hosting](#hosting)
5. [Pipelines and Deployment with Orchest and Clarify](#orchest)
6. [Email notifications of anomaly data points with Clarify using Orchest!](#email)

<a name="intro"></a>

## Introduction

In the introduction notebook you will get familiarised with the basics of interfacing with Clarify using python.

Topics covered:

- Connecting to Clarify using the PyClarify SDK
- Reading data from Clarify
- Creating Signals and Items
- Sending data back to Clarify
- Publishing Signals and creating Timelines

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/clarify/data-science-tutorials/blob/main/tutorials/Introduction.ipynb)

## <a name="forecasting"></a> Forecasting

In the Forecasting tutorial you will learn how to use data from Clarify for forecasting. We will present the steps to read and prepare the data, use a forecasting method (via the [`merlion`](https://github.com/salesforce/Merlion) library) and write the results back in Clarify.

Topics covered:

- Readind data and meta-data from Clarify
- Apply a forecasting method
- Write the forecast in Clarify
- Visualize the forecast in Clarify

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/clarify/data-science-tutorials/blob/main/tutorials/Forecasting.ipynb)

<a name="pattern"></a>

## Pattern Recognition

In the pattern recognition notebook you will gain a deeper understanding how to bring Clarify and data-science together. We will show you how to apply a pattern recognition algorithm on your data and create items with your results. After that you will be able to share your knowledge and discoveries with other members from your organization.

Topics covered:

- Read Item data from Clarify
- Apply a Pattern Recognition Algorithm
- Create Patterns
- Write signals to Clarify
- Visualise and share your results in Clarify

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/clarify/data-science-tutorials/blob/main/tutorials/Pattern%20Recognition.ipynb)

<a name="hosting"></a>

## Google Cloud Hosting

In the Google Cloud hosting notebook you will be introduced to a way for writing data to Clarify continuously using an external API of your choice.

Topics covered:

- Choose an API from where you will get your data
- Integrating with Clarify
- Create a docker image
- Google Cloud Hosting
- See results in Clarify

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/clarify/data-science-tutorials/blob/main/tutorials/Google%20Cloud%20Hosting.ipynb)

<a name="orchest"></a>

## Pipelines and Deployment with Orchest and Clarify

In this notebook you will learn how to combine [Clarify](https://www.clarify.io/) for data exploration, visualization and collaboration with [Orchest](https://www.orchest.io/) for data pipelines development and deployment.

Topics covered:

- Quickstart importing the example project and pipeline
- Pipelines in Orchest
- Read, write and forecast nodes
- Configuring recurring tasks
- Visualizing the results in Clarify

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/clarify/data-science-tutorials/blob/main/tutorials/Orchest.ipynb)

<a name="email"></a>

## Email notifications of anomaly data points with Clarify using Orchest!

In this notebook you will learn how to do anomaly detection of your data in [Clarify](https://www.clarify.io/) and get email notifications whenever an anomaly occurs, using [Orchest](https://www.orchest.io/) pipelines.

Topics covered:

- Import a Project from github and Inspect the pipepline
- Do anomaly detection
- Create a job
- View results in Clarify and receive email notifications

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/clarify/data-science-tutorials/blob/main/tutorials/Email%20notifications.ipynb)
