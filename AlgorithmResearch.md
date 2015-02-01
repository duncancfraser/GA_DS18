#Introducing the Apriori Algorithm

**Solves for:**

* 

**How it works:**

* The algorithm addresses the problem in two steps:
  1. Identify frequent itemsets in the data. *For example, in a pharmacy transaction dataset, what groups of purchases appear together frequently for customers?*
  2.  Mathematically describe the relationship between the different items in the itemset.  *For example, if a common itemset includes a toothbrush, toothpaste and mouthwash, given two of those items are were purchased, what is the probability the third will also be purchased?*

**Application Overview**

No. | Application          | Business Question 
-------------------------------------------------------------------------------------------------------------------------------------------
1.  | CRM Messenging       | How can a brand anticipate customer wants based on common combinations of purchases and message accordingly?
2.  | Savings offer bundle | Given a diverse, related product line, what products should be bundled in coupons to increase sales?
3.  | Product placement    | What products should be placed together on a store shelf based on customer purchasing behavior?

* *Details:*

  1. A travel service wants to understand based on past bookings, what other cities customers are likely to travel to.  The company wants to use this to email relevant suggestions to customers to encourage more use of the service.  It may reveal that customers who book in San Francisco, CA and Austin, TX have a 70% probability of later booking in Portland, OR.  The service can then use this to message people who recently booked in those two cities about their offerings in Portland, OR.
  2. A CPG company wants to boost sales of it's all-surface cleaner.  Surprisingly the association analysis shows that only 40% of customers who purchase paper towels and sponges also purchase the cleaner.  The CPG company can use this to include a bundle coupon where a discount is offered for the cleaner with the purchase of paper towels and sponges.
  3. A grocer wants to optimize its store design and shelving based on customer behavior for a new location.  They can use this analysis type to itentify bundles of items that should be placed near one another or in sequence throughout the store.  Purchasers of frozen pizzas and hot pockets may also often buy Ben and Jerry's ice cream, in which case the store would want to put these items in sequence within the frozens section of the store.