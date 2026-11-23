src=open('tools/newspapers2.py').read(); exec(src[:src.index("P='photos/photo_{}.png'")])
P='photos2/photo_{}.png'
DP=("The Daily Pint","“ALL THE NEWS THAT'S FIT TO DRINK”","PRICE: 1 GLASS")
DH=("The Dairy Herald","EST. BEFORE THE CRISIS","2 PINTS")
UT=("The Udder Times","LATE EDITION","1/2 PINT")
EM=("The Evening Moo","EVENING EDITION","FREE (WITH PURCHASE OF MILK)")
def p(f,paper_,no,h,sub,ph,cap,lead,seed,side=None): paper(f,*paper_,no,h,sub,P.format(ph),cap,lead,seed,side,top=(ph==4))
p('newspaper_daily-pint_great-milk-rush-begins_1024x1448.png',DP,0,"THE GREAT MILK RUSH BEGINS",
  "Shoppers strip dairy aisles bare · nobody can say why · “I just really want milk,” says customer",1,
  "Shoppers empty the dairy aisle of a supermarket on the first morning of the rush. The store had been fully stocked an hour earlier.",
  "NATIONAL — Milk sold out in supermarkets across the country on Monday as shoppers rushed to buy every bottle and carton available. Experts have no explanation. “I don't know why. I just really want milk,” said one customer, holding six bottles. The rush began shortly after the first KD-PX products went on sale. VPK Industries called the timing “a curiosity”.",11)
p('newspaper_dairy-herald_second-milk-aisle_1024x1448.png',DH,3,"SHOPS OPEN SECOND MILK AISLE",
  "Sales double, then double again · third aisle “under consideration” · shelf-stackers work around the clock",2,
  "A shop assistant fills a newly built milk aisle while customers reach past him for the cartons.",
  "RETAIL — With milk sales doubling for the second week in a row, supermarket chains have begun converting entire aisles to dairy. “We moved the bread to make room. Nobody noticed,” said one manager. A third aisle is under consideration. Shelf-stackers report that cartons rarely stay on the shelf for more than a few seconds.",12)
p('newspaper_udder-times_cows-require-bodyguards_1024x1448.png',UT,3,"COWS NOW REQUIRE BODYGUARDS",
  "New law: licence, security detail and waiting list for every cow · owners hire former celebrity guards",3,
  "A licensed dairy cow is escorted through the city centre by her personal security detail.",
  "LAW — Under new regulations announced on Friday, every cow must be accompanied by at least two licensed bodyguards when in public. Owners must also hold a cow licence; the waiting list currently stands at eleven years. “She is worth more than the building she lives in,” explained one owner, as his cow was led past a growing crowd.",13)
p('newspaper_evening-moo_pastures-declared-sacred_1024x1448.png',EM,3,"PASTURES DECLARED SACRED",
  "Grazing grounds become places of worship · candles, flowers and kneeling crowds · walking in front of a cow now “considered rude”",4,
  "Worshippers kneel before a cow on a decorated pasture. Visitors are asked to remain silent while she grazes.",
  "FAITH — Pastures across the country were declared sacred grounds this week, as growing numbers of people began to gather around cows to pray, light candles and leave flowers. Officials remind visitors that walking in front of a cow is now considered rude, and that photography is only allowed from a respectful distance.",14)
p('newspaper_dairy-herald_last-soda-plant-closes_1024x1448.png',DH,4,"LAST SODA PLANT CLOSES",
  "Bottling lines fall silent · “We could not give it away,” says former manager · site to become a dairy",5,
  "The bottling hall of the country's last soft drink plant, on the morning after its closure.",
  "INDUSTRY — The last remaining soft drink factory in the country stopped production on Wednesday. The bottles on the conveyor belt were the last ever filled; none were sold. “We could not give it away,” said a former manager. The site will reopen as a dairy. VPK Industries expressed its sympathy and repeated that it was “not involved”.",15)
p('newspaper_udder-times_counterfeit-milk-ring_1024x1448.png',UT,4,"COUNTERFEIT MILK RING BUSTED",
  "Police seize white paint, water and “optimism” · hundreds of fake bottles recovered · tasters hospitalised",6,
  "A police officer holds up a sample of the seized counterfeit milk. The real milk on the right is kept as a reference, under guard.",
  "CRIME — Police have broken up a criminal network selling counterfeit milk made from white paint, water and what officers described as “optimism”. Hundreds of fake bottles were seized. Several customers who tasted the product are recovering in hospital. Investigators warn the public to buy milk only from licensed dairies.",16)
p('newspaper_evening-moo_salaries-paid-in-litres_1024x1448.png',EM,4,"SALARIES NOW PAID IN LITRES",
  "Workers welcome “the only currency worth having” · payday queues lengthen · banks install refrigerators",7,
  "Factory workers queue at the pay window to collect their monthly wages, in milk.",
  "ECONOMY — A growing number of employers have started paying wages in milk instead of money, after staff refused to accept currencies that “cannot be drunk”. Workers collect their pay in bottles at the end of each month. Banks are installing refrigerated vaults to keep up with demand for savings accounts.",17)
p('newspaper_daily-pint_vpk-unveils-lactokd_1024x1448.png',DP,4,"VPK UNVEILS LACTOKD™",
  "Synthetic milk “in unlimited quantities” · standing ovation at launch · “The end of the shortage,” says VPK",8,
  "A VPK Industries presenter raises the first carton of LactoKd™ at the product launch.",
  "BUSINESS — VPK Industries today unveiled LactoKd™ (KD-PX-019), a synthetic Kdanium milk that the company says can be produced in unlimited quantities. “This is the end of the shortage,” the presenter told a cheering audience. Early testers described the taste as “perfect” and immediately asked for two more glasses of real milk.",18)
p('newspaper_udder-times_inside-vpk-research-herd_1024x1448.png',UT,5,"INSIDE THE VPK RESEARCH HERD",
  "404 identical cows, each serial-numbered · “For research purposes only” · all of them named Daniella K.",9,
  "Rare photograph from inside the VPK research barn. The company later stated that the photographer “was not there”.",
  "INVESTIGATION — This newspaper has obtained a rare look inside the research herd of VPK Industries: exactly 404 cows, kept in perfectly straight rows, each with a numbered ear tag and each called Daniella K. VPK Industries says the herd is used “for research purposes only” and declined to say what happens to the milk.",19)
print('ok')
