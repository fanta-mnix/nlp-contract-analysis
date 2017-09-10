# Using Machine Learning to Detect Unfair Contract Terms

Capstone Proposal for Udacity Machine Learning Nanodegree Program.

## Domain Background
When you think of the legal industry, what is the first thing that comes to your mind? Machine Learning? Probably not. When I started working in the industry as a Data Scientist one year ago, I was met with suspicion by lawyer colleagues who were eager to point out reasons why a computer wouldn't be able to do their jobs. It turns out that they were right sometimes, but not all of the time, fortunately.

Why is it fortunate? Aside from keeping my job, Brazilian Courts have reached [99.7 million pending lawsuits in 2014](http://www.cnj.jus.br/files/conteudo/arquivo/2015/11/491328c33144833370f375278683f955.pdf) and numbers continue to increase. Machine Learning can help companies stay competitive in this scenario of increasing litigation costs by freeing lawyers (and other knowledge workers) from menial, laborous and often error-prone tasks in order to focus on work that require high-order reasoning.

Beyond automation of simple tasks, Machine Learning can also be used to augment knowledge workers performance by providing complementary context to the task at hand, such as:

- Highligh important information in a document
- Search for documents according to a query
- Recommend related documents

This processes is usually refered to as [Technology Assisted Review](http://www.edrm.net/frameworks-and-standards/technology-assisted-review/) (TAR).

## Problem Statement
According to [The Restatement (Second) of Contracts, Section 1](http://www.repository.law.indiana.edu/ilj/vol7/iss7/2),
> A contract is a promise or a set of promises for the breach of which the law gives a remedy, or the performance of which the law in some way recognizes as a duty

Put it simply, a contract is an agreement between (generally) two parties that can be enforced under the law. But what if one of the parties has substantial advantages (bargaining power, knowledge) over the other and makes use of them to dictate terms that are mostly one-sided?

Contracts crafted this way are called *Unconscionable* and can be voided by a court if the exploitation is too great. For cases that are not so extreme, though, not much can be done except for paying attention to what is written in the terms before signing the contract.

To avoid problems like that, one could hire a lawyer in order to get contracts scrutinized, but it would prove too much of a hassle for people contracting Wireless Services or Insurance, for example. This project aims to help people not familiar with law to analyze contracts in those cases where professional help is unfeasible, impractical or undesired.

