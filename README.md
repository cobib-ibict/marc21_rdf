# marc21_to_rdf

<p align="center">

<a href="https://pypi.python.org/pypi/marc21_rdf">
<img src="https://img.shields.io/pypi/v/marc21_rdf.svg" /></a>
<a href="https://travis-ci.org/drummerzzz/marc21_rdf"><img src="https://travis-ci.org/drummerzzz/marc21_rdf.svg?branch=master" /></a>
</p>

**marc21_to_rdf** é uma biblioteca Python que permite a conversão de registros no formato MARC21 para RDF (Resource Description Framework). O MARC21 é um formato amplamente utilizado para representar metadados bibliográficos em bibliotecas, enquanto o RDF é uma estrutura de dados semântica usada para representar informações na web semântica. Esta biblioteca simplifica o processo de transformação de registros MARC21 em RDF.

## Features

- Conversão fácil de registros MARC21 em RDF.
- Suporte para representar informações bibliográficas em RDF.

## Installation

You can install the **marc21_to_rdf** library using pip:

```bash
pip install git+https://github.com/cobib-ibict/marc21_rdf.git@main
```
or
```bash
pip install marc21_rdf
```

## Basic Usage
Aqui está um exemplo simples de como usar a biblioteca:

```python
from datetime import datetime
from marc21_rdf import RDF
from marc21_rdf.types import Article, Publisher

# Create an Article object with the desired data
article = Article(
        id=178,
        subject='Black various ground both avoid.',
        abstract='''
        Section two food hear. Perhaps as arrive anyone call culture open since. Today human out can. Respond drive education center sit institution magazine. Scene approach Mrs cut family event. For whether head lay. World raise federal choice specific. Ever partner capital common wall than then.
        ''',
        url='http://pinakes.ccn.com/article/178',
        publisher=Publisher(
            id=320,
            url='http://pinakes.ccn.com/320',
            first_name='Kimberly',
            last_name='Burns',
        ),
        city='Shelleyside',
        issn='123',
        language='pt-BR',
        published_at=datetime.now(),
    )

# Create an RDF object
rdf = RDF()

# Build the RDF from the Article object
rdf.build(article)

# Write the RDF to a file
rdf.write('path_name/filename')

```
## Output example

```xml
<rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
  xmlns:owl="http://www.w3.org/2002/07/owl#"
  xmlns:rdfs="http://www.w3.org/2000/01/rdf-schema#"
  xmlns:foaf="http://xmlns.com/foaf/0.1/"
  xmlns:vivo="http://vivoweb.org/ontology/core#"
  xmlns:bibo="http://purl.org/ontology/bibo/"
  xmlns:vitro="http://vitro.mannlib.cornell.edu/ns/vitro/0.7#"
  xmlns:dcterms="http://purl.org/dc/terms/"
  xmlns:dc="http://purl.org/dc/elements/1.1/"
  xmlns:obo="http://purl.obolibrary.org/obo/"
>
  <!-- Publisher -->
<rdf:Description rdf:about="http://pinakes.ccn.com/person/320">
    <rdf:type rdf:resource="http://vivoweb.org/ontology/core#Publisher" />
    <rdfs:label xml:lang="pt-BR">Kimberly Burns</rdfs:label>
    <vivo:firstName>Kimberly</vivo:firstName>
    <vivo:lastName>Burns</vivo:lastName>
    <vivo:publisherOf rdf:resource="http://pinakes.ccn.com/article/178" />
  </rdf:Description>

  <!-- Article -->
  <vivo:Article rdf:about="http://pinakes.ccn.com/article/178">
    <rdfs:label
      xml:lang="pt-BR">Black various ground both avoid.</rdfs:label>
    <vivo:Title>Black various ground both avoid.</vivo:Title>
    <vivo:freetextKeyword
    xml:lang="pt-BR">Black various ground both avoid.
    </vivo:freetextKeyword>  <vivo:freetextKeyword xml:lang="pt-BR">Black</vivo:freetextKeyword>  <vivo:freetextKeyword xml:lang="pt-BR">various</vivo:freetextKeyword>  <vivo:freetextKeyword xml:lang="pt-BR">ground</vivo:freetextKeyword>  <vivo:freetextKeyword xml:lang="pt-BR">both</vivo:freetextKeyword>  <vivo:freetextKeyword xml:lang="pt-BR">avoid.</vivo:freetextKeyword>

      <vivo:dateTime>2023-10-09T09:51:30</vivo:dateTime>
      <vivo:dateTimeValue>2023-10-09T09:51:30</vivo:dateTimeValue>

  </vivo:Article>

  <!-- Article -->
  <bibo:Article rdf:about="http://pinakes.ccn.com/article/178">
    <bibo:authorList rdf:parseType="Resource">
      <bibo:author rdf:resource="http://pinakes.ccn.com/person/320" />
    </bibo:authorList>
    <bibo:title>Black various ground both avoid.</bibo:title>

    <bibo:abstract xml:lang="pt-BR">Section two food hear. Perhaps as arrive anyone call culture open since. Today human out can. Respond drive education center sit institution magazine. Scene approach Mrs cut family event. For whether head lay. World raise federal choice specific. Ever partner capital common wall than then.</bibo:abstract>


      <vivo:dateTime>2023-10-09T09:51:30</vivo:dateTime>
      <vivo:dateTimeValue>2023-10-09T09:51:30</vivo:dateTimeValue>

  </bibo:Article>
  <!-- City -->
  <rdf:Description rdf:about="http://pinakes.ccn.com/article/178">
    <rdf:type rdf:resource="http://vitro.mannlib.cornell.edu/ns/vitro/public#Location" />
    <vitro:locationName>Shelleyside</vitro:locationName>
    <vivo:placeOfPublication xml:lang="pt-BR"> Shelleyside </vivo:placeOfPublication>
  </rdf:Description>
  <vivo:Authorship rdf:about="/publishers/761/articles/690">
    <vivo:relates rdf:resource="http://pinakes.ccn.com/person/320"/>
    <vivo:relates rdf:resource="http://pinakes.ccn.com/article/178"/>
  </vivo:Authorship>
</rdf:RDF>
```

Certifique-se de substituir os dados de exemplo pelos seus próprios dados bibliográficos. Esta é apenas uma introdução básica, e você pode personalizar ainda mais a conversão e o uso da biblioteca de acordo com suas necessidades específicas. Consulte a documentação completa para obter informações detalhadas sobre os recursos e opções disponíveis.
