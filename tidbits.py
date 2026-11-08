"""For (hopefully) historical tidbits of information"""
sources = [
  "https://www.gutenberg.org/cache/epub/57493/pg57493.txt", #The Natural History of Pliny, Volume 1 (of 6) by the Elder Pliny
  "https://www.gutenberg.org/cache/epub/60230/pg60230.txt", #The Natural History of Pliny, Volume 2 (of 6) by the Elder Pliny
  "https://www.gutenberg.org/cache/epub/59131/pg59131.txt", #The Natural History of Pliny, Volume 3 (of 6) by the Elder Pliny
  "https://www.gutenberg.org/cache/epub/61113/pg61113.txt", #The Natural History of Pliny, Volume 4 (of 6) by the Elder Pliny
  "https://www.gutenberg.org/cache/epub/60688/pg60688.txt", #The Natural History of Pliny, Volume 5 (of 6) by the Elder Pliny
  "https://www.gutenberg.org/cache/epub/62704/pg62704.txt", #The Natural History of Pliny, Volume 6 (of 6) by the Elder Pliny
  "https://www.gutenberg.org/cache/epub/58589/pg58589.txt", #The Boys' and Girls' Pliny by the Elder Pliny
  "https://www.gutenberg.org/cache/epub/26000/pg26000.txt", #The Sailor's Word-Book by W. H. Smyth
  "https://www.gutenberg.org/cache/epub/42474/pg42474.txt", #1000 Mythological Characters Briefly Described by Edward Sylvester Ellis
  "https://www.gutenberg.org/cache/epub/55059/pg55059.txt", #Modern English biography, volume 1 (of 6), A-H by Frederic Boase
  "https://www.gutenberg.org/cache/epub/71046/pg71046.txt", #Modern English biography, volume 2 (of 6), I-Q by Frederic Boase
  "https://www.gutenberg.org/cache/epub/20776/pg20776.txt", #Encyclopedia of Needlework by Thérèse de Dillmont
  "https://www.gutenberg.org/cache/epub/44562/pg44562.txt", #A Dictionary of Arts, Manufactures and Mines by Andrew Ure
  "https://www.gutenberg.org/cache/epub/10766/pg10766.txt", #Enquire within upon everything by Robert Kemp Philp
  "https://www.gutenberg.org/cache/epub/21682/pg21682.txt", #The field and garden vegetables of America : containing full descriptions of…
  "https://www.gutenberg.org/cache/epub/5402/pg5402.txt",   #1811 Dictionary of the Vulgar Tongue by Francis Grose
  "https://www.gutenberg.org/cache/epub/47018/pg47018.txt", #A Dictionary of Slang, Cant, and Vulgar Words by John Camden Hotten
  "https://www.gutenberg.org/cache/epub/2108/pg2108.txt",   #The slang dictionary : Etymological, historical and anecdotal by Hotten
  "https://www.gutenberg.org/cache/epub/45249/pg45249.txt", #The History of Signboards, from the Earliest times to the Present Day by Larwood et al.
  "https://www.gutenberg.org/cache/epub/44028/pg44028.txt", #The Every Day Book of History and Chronology by Joel Munsell
  "https://www.gutenberg.org/cache/epub/70718/pg70718.txt", #The inter ocean curiosity shop for the year 1883 by Various
  "https://www.gutenberg.org/cache/epub/747/pg747.txt",     #Anomalies and Curiosities of Medicine by George M. Gould and Walter L. Pyle
  "https://www.gutenberg.org/cache/epub/39733/pg39733.txt", #Cooley's Cyclopædia of Practical Receipts and Collateral Information in the…
  "https://www.gutenberg.org/cache/epub/41957/pg41957.txt", #Cooley's Cyclopædia of Practical Receipts and Collateral Information in the…
  "https://www.gutenberg.org/cache/epub/26535/pg26535.txt", #The Standard Electrical Dictionary by T. O'Conor Sloane
  "https://www.gutenberg.org/cache/epub/12513/pg12513.txt", #A Classification and Subject Index for Cataloguing and Arranging the Books and…
  "https://www.gutenberg.org/cache/epub/61526/pg61526.txt", #A Dictionary of Islam by Thomas Patrick Hughes
  "https://www.gutenberg.org/cache/epub/47682/pg47682.txt", #American Book-Plates: A Guide to Their Study with Examples by Charles Dexter Allen
  "https://www.gutenberg.org/cache/epub/28900/pg28900.txt", #English Synonyms and Antonyms by James Champlin Fernald
  "https://www.gutenberg.org/cache/epub/41697/pg41697.txt", #Merck's 1899 Manual of the Materia Medica by Merck & Co.
  "https://www.gutenberg.org/cache/epub/41140/pg41140.txt", #Bible Atlas: A Manual of Biblical Geography and History by Jesse Lyman Hurlbut
  "https://www.gutenberg.org/cache/epub/57705/pg57705.txt", #An Universal Dictionary of the Marine by William Falconer
  "https://www.gutenberg.org/cache/epub/59959/pg59959.txt", #English Surnames: Their Sources and Significations by Bardsley
  "https://www.gutenberg.org/cache/epub/39284/pg39284.txt", #Curiosities of Puritan Nomenclature by Charles Wareing Endell Bardsley
  "https://www.gutenberg.org/cache/epub/51739/pg51739.txt", #The Romance of the London Directory by Charles Wareing Endell Bardsley
  "https://www.gutenberg.org/cache/epub/74739/pg74739.txt", #A military dictionary : or, Explanation of the several systems of discipline…
  "https://www.gutenberg.org/cache/epub/62250/pg62250.txt", #History, Gazetteer, and Directory of Shropshire [1851] by Samuel Bagshaw
  "https://www.gutenberg.org/cache/epub/71324/pg71324.txt", #A dictionary of American authors by Oscar Fay Adams
  "https://www.gutenberg.org/cache/epub/37072/pg37072.txt", #A Brief Handbook of English Authors by Oscar Fay Adams
  "https://www.gutenberg.org/cache/epub/78263/pg78263.txt", #Slang and its analogues past and present, volume 1 [of 7] : A dictionary,…
  "https://www.gutenberg.org/cache/epub/77292/pg77292.txt", #Slang and its analogues past and present, volume 2 [of 7] : A dictionary,…
  "https://www.gutenberg.org/cache/epub/74870/pg74870.txt", #Slang and its analogues past and present, volume 3 [of 7] : A dictionary,…
  "https://www.gutenberg.org/cache/epub/79663/pg79663.txt", #Slang and its analogues past and present, volume 4 [of 7] : A dictionary,…
  "https://www.gutenberg.org/cache/epub/68769/pg68769.txt", #A classical dictionary by John Lemprière
  "https://www.gutenberg.org/cache/epub/59563/pg59563.txt", #A Military Dictionary and Gazetteer by Thomas Wilhelm
  "https://www.gutenberg.org/cache/epub/42172/pg42172.txt", #Every Boy's Book: A Complete Encyclopædia of Sports and Amusements by Routledge
  "https://www.gutenberg.org/cache/epub/70427/pg70427.txt", #History for ready reference, Volumes 1 to 5 by J. N. Larned
  "https://www.gutenberg.org/cache/epub/14472/pg14472.txt", #Showell's Dictionary of Birmingham by Thomas T. Harman and Walter Showell
  "https://www.gutenberg.org/cache/epub/51104/pg51104.txt", #Allen & Morton's West-London Directory for 1867 by Allen & Morton
  "https://www.gutenberg.org/cache/epub/38390/pg38390.txt", #A Dictionary of English Synonymes and Synonymous or Parallel Expressions by Soule
  "https://www.gutenberg.org/cache/epub/67629/pg67629.txt", #An Illustrated Dictionary of Words used in Art and Archaeology by John W. Mollett
  "https://www.gutenberg.org/cache/epub/34513/pg34513.txt", #A Biographical Dictionary of Freethinkers of All Ages and Nations by J. M. Wheeler
  "https://www.gutenberg.org/cache/epub/52930/pg52930.txt", #Names: and Their Meaning; A Book for the Curious by Leopold Wagner
  "https://www.gutenberg.org/cache/epub/14091/pg14091.txt", #Barkham Burroughs' Encyclopaedia of Astounding Facts and Useful Information,…
  "https://www.gutenberg.org/cache/epub/53884/pg53884.txt", #A Biblical and Theological Dictionary by Richard Watson
  "https://www.gutenberg.org/cache/epub/70957/pg70957.txt", #The treasury of languages : A rudimentary dictionary of universal philology
  "https://www.gutenberg.org/cache/epub/65909/pg65909.txt", #A Smaller Dictionary of Greek and Roman Antiquities by William Smith
  "https://www.gutenberg.org/cache/epub/2096/pg2096.txt",   #A Smaller History of Greece: from the Earliest Times to the Roman Conquest by Smith
  "https://www.gutenberg.org/cache/epub/19694/pg19694.txt", #A Smaller History of Rome by William Smith and Eugene Lawrence
  "https://www.gutenberg.org/cache/epub/71502/pg71502.txt", #American politics (non-partisan) from the beginning to date : embodying…
  "https://www.gutenberg.org/cache/epub/15191/pg15191.txt", #The Commercial Products of the Vegetable Kingdom by P. L. Simmonds
  "https://www.gutenberg.org/cache/epub/71509/pg71509.txt", #The curiosities of food : or, The dainties and delicacies of different nations…
  "https://www.gutenberg.org/cache/epub/57340/pg57340.txt", #Coffee and chicory : Their culture, chemical composition, preparation for…
  "https://www.gutenberg.org/cache/epub/49912/pg49912.txt", #The Employments of Women: A Cyclopædia of Woman's Work by Virginia Penny
  "https://www.gutenberg.org/cache/epub/52320/pg52320.txt", #Vocabulum; or The Rogue's Lexicon by George W. Matsell
  "https://www.gutenberg.org/cache/epub/64006/pg64006.txt", #Rogers' Directory of Norwich and Neighbourhood by Edmund Dawson Rogers
  "https://www.gutenberg.org/cache/epub/76850/pg76850.txt", #The watchmakers' hand book : intended as a workshop companion for those…
  "https://www.gutenberg.org/cache/epub/53336/pg53336.txt", #The Public School Word-book by John Stephen Farmer
  "https://www.gutenberg.org/cache/epub/30323/pg30323.txt", #The Book of Religions by John Hayward
  "https://www.gutenberg.org/cache/epub/49791/pg49791.txt", #Miscellanea Curiosa, Vol. 1 by Edmond Halley et al.
  "https://www.gutenberg.org/cache/epub/43991/pg43991.txt", #A Hand-book to the Primates, Volume 1 (of 2) by Henry O. Forbes
  "https://www.gutenberg.org/cache/epub/43992/pg43992.txt", #A Hand-book to the Primates, Volume 2 (of 2) by Henry O. Forbes
  "https://www.gutenberg.org/cache/epub/75040/pg75040.txt", #The wonders of the world : a complete museum, descriptive and pictorial, of…
  "https://www.gutenberg.org/cache/epub/14403/pg14403.txt", #1001 Questions and Answers on Orthography and Reading by B. A. Hathaway
  "https://www.gutenberg.org/cache/epub/45809/pg45809.txt", #A Glossary of Words used in the Country of Wiltshire by Dartnell and Goddard
  "https://www.gutenberg.org/cache/epub/59215/pg59215.txt", #Rules for a Dictionary Catalogue by Charles A. Cutter
  "https://www.gutenberg.org/cache/epub/58160/pg58160.txt", #Allen's West London Street Directory, 1868 by Samuel Allen
  "https://www.gutenberg.org/cache/epub/38457/pg38457.txt", #Alden's Handy Atlas of the World by John B. Alden
  "https://www.gutenberg.org/cache/epub/60729/pg60729.txt", #Slater's [1859] Shropshire Directory by I. Slater
  "https://www.gutenberg.org/cache/epub/57783/pg57783.txt", #The Legislative Manual, of the State of Colorado by Thomas B. Corbett
  "https://www.gutenberg.org/cache/epub/28413/pg28413.txt", #The Student's Companion to Latin Authors by George Middleton and Thomas Ross Mills
  "https://www.gutenberg.org/cache/epub/25212/pg25212.txt", #A Glossary of Provincial Words & Phrases in use in Somersetshire by Williams
  "https://www.gutenberg.org/cache/epub/56162/pg56162.txt", #The Illustrated Dictionary of Gardening, Division 1; A to Car. by George Nicholson et al.
  "https://www.gutenberg.org/cache/epub/14968/pg14968.txt", #The Standard Operas: Their Plots, Their Music, and Their Composers by Upton
  "https://www.gutenberg.org/cache/epub/22793/pg22793.txt", #The Standard Oratorios: Their Stories, Their Music, And Their Composers by Upton
  "https://www.gutenberg.org/cache/epub/32248/pg32248.txt", #The Standard Cantatas: Their Stories, Their Music, and Their Composers by Upton
  "https://www.gutenberg.org/cache/epub/67827/pg67827.txt", #Life of Haydn by Ludwig Nohl
  "https://www.gutenberg.org/cache/epub/36734/pg36734.txt", #The Browning Cyclopædia: A Guide to the Study of the Works of Robert Browning
  "https://www.gutenberg.org/cache/epub/59821/pg59821.txt", #Handbook of the new Library of Congress by Small, Caffin, and Spofford
  "https://www.gutenberg.org/cache/epub/44460/pg44460.txt", #Carleton's Condensed Classical Dictionary by George Washington Carleton
  "https://www.gutenberg.org/cache/epub/23852/pg23852.txt", #Canadian Postal Guide by Canada. Post Office Department
  "https://www.gutenberg.org/cache/epub/53084/pg53084.txt", #A manual of Italian literature by Francis Henry Cliffe
  "https://www.gutenberg.org/cache/epub/63912/pg63912.txt", #The American Encyclopedia of History, Biography and Travel by Thomas H. Prescott
  "https://www.gutenberg.org/cache/epub/54233/pg54233.txt", #The Vivisectors' Directory by Benjamin Bryan and Frances Power Cobbe
  "https://www.gutenberg.org/cache/epub/62386/pg62386.txt", #Melville and Co.'s Directory and Gazetteer of Norwich, Yarmouth, Dereham,…
  "https://www.gutenberg.org/cache/epub/32829/pg32829.txt", #A concise history and directory of the city of Norwich for 1811 by Berry
  "https://www.gutenberg.org/cache/epub/58200/pg58200.txt", #Lakeland Words by Bryham Kirkby
  "https://www.gutenberg.org/cache/epub/17265/pg17265.txt", #Companion to the Bible by E. P. Barrows
  "https://www.gutenberg.org/cache/epub/62401/pg62401.txt", #Mason's Norwich General and Commercial Directory & Handbook by R. Hindry Mason
  "https://www.gutenberg.org/cache/epub/49524/pg49524.txt", #Knowledge for the Time by John Timbs
  "https://www.gutenberg.org/cache/epub/48516/pg48516.txt", #Curiosities of Science, Past and Present by John Timbs
  "https://www.gutenberg.org/cache/epub/61084/pg61084.txt", #The Standard Manual for Baptist Churches by Edward T. Hiscox
  "https://www.gutenberg.org/cache/epub/12864/pg12864.txt", #A Collection of College Words and Customs by Benjamin Homer Hall
  "https://www.gutenberg.org/cache/epub/57898/pg57898.txt", #Useful Knowledge: Volume 1. Minerals by William Bingley
  "https://www.gutenberg.org/cache/epub/57954/pg57954.txt", #Useful Knowledge: Volume 2. Vegetables by William Bingley
  "https://www.gutenberg.org/cache/epub/58118/pg58118.txt", #Useful Knowledge: Volume 3. Animals by William Bingley
  "https://www.gutenberg.org/cache/epub/60126/pg60126.txt", #Pens and types : or, Hints and helps for those who write, print, read, teach,…
  "https://www.gutenberg.org/cache/epub/70210/pg70210.txt", #A select glossary of English words used formerly in senses different from their…
  "https://www.gutenberg.org/cache/epub/8163/pg8163.txt",   #Handbook of Universal Literature, From the Best and Latest Authorities by Botta
  "https://www.gutenberg.org/cache/epub/17712/pg17712.txt", #The moon : a full description and map of its principal physical features by Elger
  "https://www.gutenberg.org/cache/epub/2468/pg2468.txt",   #Repertory of The Comedie Humaine, Part 1 by Cerfberr and Christophe
  "https://www.gutenberg.org/cache/epub/2469/pg2469.txt",   #Repertory of The Comedie Humaine, Part 2 by Cerfberr and Christophe
  "https://www.gutenberg.org/cache/epub/47367/pg47367.txt", #British Pomology by Robert Hogg
  "https://www.gutenberg.org/cache/epub/65002/pg65002.txt", #The Birds of Australia, Vol. 1 of 7 by John Gould
  "https://www.gutenberg.org/cache/epub/60302/pg60302.txt", #The Birds of Australia, Vol. 2 of 7 by John Gould
  "https://www.gutenberg.org/cache/epub/60646/pg60646.txt", #The Birds of Australia, Vol. 3 of 7 by John Gould
  "https://www.gutenberg.org/cache/epub/60833/pg60833.txt", #The Birds of Australia, Vol. 4 of 7 by John Gould
  "https://www.gutenberg.org/cache/epub/62524/pg62524.txt", #The Birds of Australia, Vol. 5 of 7 by John Gould
  "https://www.gutenberg.org/cache/epub/52232/pg52232.txt", #A Bible Hand-Book by F. C. Holliday
  "https://www.gutenberg.org/cache/epub/71466/pg71466.txt", #Queer questions and ready replies : A collection of four hundred questions in…
  "https://www.gutenberg.org/cache/epub/70907/pg70907.txt", #Catalogue of the dipterous insects collected at Singapore and Malacca by Wallace
  "https://www.gutenberg.org/cache/epub/59076/pg59076.txt", #The Sporting Dictionary, and Rural Repository, Volume 1 (of 2) by William Taplin
  "https://www.gutenberg.org/cache/epub/59291/pg59291.txt", #The Sporting Dictionary and Rural Repository, Volume 2 (of 2) by William Taplin
  "https://www.gutenberg.org/cache/epub/75849/pg75849.txt", #Aggravating ladies : Being a list of works published under the pseudonym of "a…
  "https://www.gutenberg.org/cache/epub/9916/pg9916.txt",   #Spalding's Baseball Guide and Official League Book for 1895 by Henry Chadwick
  "https://www.gutenberg.org/cache/epub/65710/pg65710.txt", #A Synopsis of the British Mosses by Charles C. P. Hobkirk
  "https://www.gutenberg.org/cache/epub/31165/pg31165.txt", #The Church Handy Dictionary by Anonymous
  "https://www.gutenberg.org/cache/epub/15484/pg15484.txt", #The Care and Feeding of Children by L. Emmett Holt
  "https://www.gutenberg.org/cache/epub/14551/pg14551.txt", #A catechism of Christian doctrine, no. 1 : for first communion classes
  "https://www.gutenberg.org/cache/epub/14552/pg14552.txt", #A catechism of Christian doctrine, no. 2 : for confirmation classes by De Concilio et al.
  "https://www.gutenberg.org/cache/epub/14553/pg14553.txt", #A catechism of Christian doctrine, no. 3 : for two years' course for post-…
  "https://www.gutenberg.org/cache/epub/16728/pg16728.txt", #A Catechism of Familiar Things; by Anonymous
  "https://www.gutenberg.org/cache/epub/76379/pg76379.txt", #Catechism of the locomotive by Matthias N. Forney and Georg Kosak
  "https://www.gutenberg.org/cache/epub/10998/pg10998.txt", #A Catechism of the Steam Engine by C. E. John Bourne
  "https://www.gutenberg.org/cache/epub/59133/pg59133.txt", #A Body of Divinity, Vol. 1 (of 4) by Thomas Ridgley
  "https://www.gutenberg.org/cache/epub/62149/pg62149.txt", #A Body of Divinity, Vol. 2 (of 4) by Thomas Ridgley
  "https://www.gutenberg.org/cache/epub/64185/pg64185.txt", #A Body of Divinity, Vol. 3 (of 4) by Thomas Ridgley
  "https://www.gutenberg.org/cache/epub/65484/pg65484.txt", #A Body of Divinity, Vol. 4 (of 4) by Thomas Ridgley
  "https://www.gutenberg.org/cache/epub/69376/pg69376.txt", #Anti-slavery catechism by Lydia Maria Child
  "https://www.gutenberg.org/cache/epub/39293/pg39293.txt", #The Gentlemen's Book of Etiquette and Manual of Politeness by Cecil B. Hartley
  "https://www.gutenberg.org/cache/epub/23860/pg23860.txt", #The Young Man's Guide by William A. Alcott
  "https://www.gutenberg.org/cache/epub/27394/pg27394.txt", #A New Guide for Emigrants to the West by John Mason Peck
  "https://www.gutenberg.org/cache/epub/14400/pg14400.txt", #Manual of Egyptian Archaeology and Guide to the Study of Antiquities in Egypt
  "https://www.gutenberg.org/cache/epub/57630/pg57630.txt", #Spons' Household Manual by E. & F. N. Spon
  "https://www.gutenberg.org/cache/epub/69487/pg69487.txt", #The complete servant by servant Samuel Adams and Sarah Adams
  "https://www.gutenberg.org/cache/epub/26597/pg26597.txt", #How to Behave: A Pocket Manual of Republican Etiquette, and Guide to Correct…
  "https://www.gutenberg.org/cache/epub/6598/pg6598.txt",   #American Woman's Home: Or, Principles of Domestic Science; by Beecher and Stowe
  "https://www.gutenberg.org/cache/epub/21829/pg21829.txt", #A Treatise on Domestic Economy; For the Use of Young Ladies at Home and at…
  "https://www.gutenberg.org/cache/epub/4337/pg4337.txt",   #Power Through Repose by Annie Payson Call
  "https://www.gutenberg.org/cache/epub/4385/pg4385.txt",   #As a Matter of Course by Annie Payson Call
  "https://www.gutenberg.org/cache/epub/41279/pg41279.txt", #The Butterfly Book by W. J. Holland
  "https://www.gutenberg.org/cache/epub/43614/pg43614.txt", #The Valleys of Tirol: Their traditions and customs and how to visit them by Busk
  "https://www.gutenberg.org/cache/epub/19924/pg19924.txt", #Plain Facts for Old and Young by John Harvey Kellogg
  "https://www.gutenberg.org/cache/epub/17367/pg17367.txt", #First Book in Physiology and Hygiene by John Harvey Kellogg
  "https://www.gutenberg.org/cache/epub/74519/pg74519.txt", #The uses of water in health and disease : A practical treatise on the bath,…
  "https://www.gutenberg.org/cache/epub/13923/pg13923.txt", #The Whitehouse Cookbook (1887) by F. L. Gillette and Hugo Ziemann
  "https://www.gutenberg.org/cache/epub/20889/pg20889.txt", #Facts About Champagne and Other Sparkling Wines by Henry Vizetelly
  "https://www.gutenberg.org/cache/epub/46953/pg46953.txt", #A History of Champagne, with Notes on the Other Sparkling Wines of France
  "https://www.gutenberg.org/cache/epub/57168/pg57168.txt", #The Land Beyond the Forest: Facts, Figures, and Fancies from Transylvania by Gerard
  "https://www.gutenberg.org/cache/epub/41625/pg41625.txt", #Curious Facts in the History of Insects; Including Spiders and Scorpions. by Cowan
  "https://www.gutenberg.org/cache/epub/51034/pg51034.txt", #The Invention of Printing. by Theodore Low De Vinne
  "https://www.gutenberg.org/cache/epub/35123/pg35123.txt", #The Ladies' Book of Etiquette, and Manual of Politeness by Florence Hartley
  "https://www.gutenberg.org/cache/epub/50750/pg50750.txt", #The Officer's Manual: Napoleon's Maxims of War by Emperor of the French Napoleon I
  "https://www.gutenberg.org/cache/epub/46254/pg46254.txt", #Mrs. Hale's Receipts for the Million by Sarah Josepha Buell Hale
  "https://www.gutenberg.org/cache/epub/75494/pg75494.txt", #The workwoman's guide : containing instructions to the inexperienced in…
  "https://www.gutenberg.org/cache/epub/9097/pg9097.txt",   #Robert's Rules of Order by Henry M. Robert
  "https://www.gutenberg.org/cache/epub/42709/pg42709.txt", #Poisons, Their Effects and Detection by Alexander Wynter Blyth
  "https://www.gutenberg.org/cache/epub/77516/pg77516.txt", #Astronomy by Agnes M. Clerke, A. Fowler, and J. Ellard Gore
  "https://www.gutenberg.org/cache/epub/40383/pg40383.txt", #Musical Myths and Facts, Volume 1 (of 2) by Carl Engel
  "https://www.gutenberg.org/cache/epub/40384/pg40384.txt", #Musical Myths and Facts, Volume 2 (of 2) by Carl Engel
  "https://www.gutenberg.org/cache/epub/45124/pg45124.txt", #Great Facts by Frederick C. Bakewell
  "https://www.gutenberg.org/cache/epub/23776/pg23776.txt", #The School of Recreation (1684 edition) by R. H.
  "https://www.gutenberg.org/cache/epub/17727/pg17727.txt", #The School of Recreation (1696 edition) by R. H.
  "https://www.gutenberg.org/cache/epub/1697/pg1697.txt",   #Madam How and Lady Why; Or, First Lessons in Earth Lore for Children by Kingsley
  "https://www.gutenberg.org/cache/epub/695/pg695.txt",     #Glaucus; Or, The Wonders of the Shore by Charles Kingsley
  "https://www.gutenberg.org/cache/epub/17437/pg17437.txt", #Health and Education by Charles Kingsley
  "https://www.gutenberg.org/cache/epub/67257/pg67257.txt", #Lessons in Sabre, Singlestick, Sabre & Bayonet, and Sword Feats by J. M. Waite
  "https://www.gutenberg.org/cache/epub/54372/pg54372.txt", #The Royal Pastime of Cock-fighting by R. H.
  "https://www.gutenberg.org/cache/epub/28681/pg28681.txt", #The Cook's Oracle; and Housekeeper's Manual by William Kitchiner
  "https://www.gutenberg.org/cache/epub/40891/pg40891.txt", #The Art of Invigorating and Prolonging Life by William Kitchiner
  "https://www.gutenberg.org/cache/epub/70726/pg70726.txt", #The traveller's oracle; or, maxims for locomotion, part 2 (of 2) : Containing…
  "https://www.gutenberg.org/cache/epub/25520/pg25520.txt", #The Stock-Feeder's Manual by Sir Charles Alexander Cameron
  "https://www.gutenberg.org/cache/epub/41595/pg41595.txt", #The Funny Side of Physic by Addison Darre Crabtre
  "https://www.gutenberg.org/cache/epub/34350/pg34350.txt", #A Manual of Elementary Geology by Sir Charles Lyell
  "https://www.gutenberg.org/cache/epub/3772/pg3772.txt",   #The Student's Elements of Geology by Sir Charles Lyell
  "https://www.gutenberg.org/cache/epub/60687/pg60687.txt", #The Magician's Own Book, or, the Whole Art of Conjuring by Arnold and Cahil
  "https://www.gutenberg.org/cache/epub/14444/pg14444.txt", #The Complete English Tradesman (1839 ed.) by Daniel Defoe
  "https://www.gutenberg.org/cache/epub/10726/pg10726.txt", #Outlines of Lessons in Botany, Part I; from Seed to Leaf by Jane Newell Moore
  "https://www.gutenberg.org/cache/epub/49155/pg49155.txt", #Marion Harland's Cookery for Beginners by Marion Harland
  "https://www.gutenberg.org/cache/epub/46144/pg46144.txt", #Six Cups of Coffee by Parloa, Campbell, Corson, Harland, Lincoln, Owen, and Poole
  "https://www.gutenberg.org/cache/epub/16800/pg16800.txt", #The Secret of a Happy Home (1896) by Marion Harland
  "https://www.gutenberg.org/cache/epub/49958/pg49958.txt", #The Dinner Year-Book by Marion Harland
  "https://www.gutenberg.org/cache/epub/49944/pg49944.txt", #Breakfast, Luncheon and Tea by Marion Harland
  "https://www.gutenberg.org/cache/epub/48804/pg48804.txt", #Common Sense in the Household: A Manual of Practical Housewifery by Marion Harland
  "https://www.gutenberg.org/cache/epub/11722/pg11722.txt", #First Lessons in Geography by James Monteith
  "https://www.gutenberg.org/cache/epub/58166/pg58166.txt", #The Art of Tying the Cravat; Demonstrated in sixteen lessons by H. Le Blanc
  "https://www.gutenberg.org/cache/epub/77859/pg77859.txt", #The starry skies : or, First lessons on the sun, moon and stars by Agnes Giberne
  "https://www.gutenberg.org/cache/epub/62871/pg62871.txt", #Thoughts on a Pebble, or, A First Lesson in Geology by Gideon Algernon Mantell
  "https://www.gutenberg.org/cache/epub/53778/pg53778.txt", #First Lessons in Natural Philosophy for Beginners by Joseph C. Martindale
  "https://www.gutenberg.org/cache/epub/75832/pg75832.txt", #First lessons in the principles of cooking by Lady Barker
  "https://www.gutenberg.org/cache/epub/71943/pg71943.txt", #Popular lessons in astronomy, on a new plan : in which some of the leading…
  "https://www.gutenberg.org/cache/epub/50903/pg50903.txt", #Sleight of Hand: A Practical Manual of Legerdemain for Amateurs & Others by Sachs
  "https://www.gutenberg.org/cache/epub/43417/pg43417.txt", #A conchological manual by G. B. Sowerby
  "https://www.gutenberg.org/cache/epub/24583/pg24583.txt", #Langstroth on the Hive and the Honey-Bee: A Bee Keeper's Manual by L. L. Langstroth
  "https://www.gutenberg.org/cache/epub/14594/pg14594.txt", #Cassell's Vegetarian Cookery: A Manual of Cheap and Wholesome Diet by A. G. Payne
  "https://www.gutenberg.org/cache/epub/61112/pg61112.txt", #A New Light of Alchymie by Michal Sedziwój and Paracelsus
  "https://www.gutenberg.org/cache/epub/68043/pg68043.txt", #Fossil plants, Vol. 1 : [A text-book] for students of botany and geology by Seward
  "https://www.gutenberg.org/cache/epub/24564/pg24564.txt", #A Manual of the Operations of Surgery by Joseph Bell
  "https://www.gutenberg.org/cache/epub/12327/pg12327.txt", #The Jewish Manual by Lady Judith Cohen Montefiore
  "https://www.gutenberg.org/cache/epub/62988/pg62988.txt", #The Complete Manual of Catholic Piety by William Gahan
  "https://www.gutenberg.org/cache/epub/71928/pg71928.txt", #The gunsmith's manual : A complete handbook for the American gunsmith, being…
  "https://www.gutenberg.org/cache/epub/71463/pg71463.txt", #Hanky Panky : A book of conjuring tricks by Wiljalba Frikell
  "https://www.gutenberg.org/cache/epub/44509/pg44509.txt", #A Manual of the Historical Development of Art by G. G. Zerffi
  "https://www.gutenberg.org/cache/epub/77729/pg77729.txt", #The kedge-anchor : or, Young sailors' assistant. by William N. Brady
  "https://www.gutenberg.org/cache/epub/68388/pg68388.txt", #How to thought-read : A manual of instruction in the strange and mystic in…
  "https://www.gutenberg.org/cache/epub/51204/pg51204.txt", #Corticelli Home Needlework, 1898: A Manual of Art, Embroidery and Knitting
  "https://www.gutenberg.org/cache/epub/61065/pg61065.txt", #Modern American Drinks: How to Mix and Serve All Kinds of Cups and Drinks
  "https://www.gutenberg.org/cache/epub/58452/pg58452.txt", #Fences, Gates and Bridges: A Practical Manual by George A. Martin
  "https://www.gutenberg.org/cache/epub/50059/pg50059.txt", #How to Behave and How to Amuse: A Handy Manual of Etiquette and Parlor Games
  "https://www.gutenberg.org/cache/epub/44096/pg44096.txt", #An elementary manual of New Zealand entomology : being an introduction to the…
  "https://www.gutenberg.org/cache/epub/44551/pg44551.txt", #New Zealand Moths and Butterflies (Macro-Lepidoptera) by G. V. Hudson
  "https://www.gutenberg.org/cache/epub/31605/pg31605.txt", #The Cooking Manual of Practical Directions for Economical Every-Day Cookery
  "https://www.gutenberg.org/cache/epub/39747/pg39747.txt", #A Manual of Ancient History by A. H. L. Heeren
  "https://www.gutenberg.org/cache/epub/68394/pg68394.txt", #The Trouvelot astronomical drawings manual by E. L. Trouvelot
  "https://www.gutenberg.org/cache/epub/71233/pg71233.txt", #Anthropology : an introduction to the study of man and civilization by Tylor
  "https://www.gutenberg.org/cache/epub/47836/pg47836.txt", #The Matron's Manual of Midwifery, and the Diseases of Women During Pregnancy…
  "https://www.gutenberg.org/cache/epub/50100/pg50100.txt", #How to Do Chemical Tricks by active 1894-1902 A. Anderson
  "https://www.gutenberg.org/cache/epub/64054/pg64054.txt", #Cameo Cutting by John B. Marsh
  "https://www.gutenberg.org/cache/epub/35329/pg35329.txt", #A Manual of the Antiquity of Man by J. P. MacLean
  "https://www.gutenberg.org/cache/epub/42982/pg42982.txt", #Photography in the studio and in the field : a practical manual designed as…
  "https://www.gutenberg.org/cache/epub/57979/pg57979.txt", #Mother, Nurse and Infant by S. P. Sackett
  "https://www.gutenberg.org/cache/epub/39500/pg39500.txt", #Beauties and Antiquities of Ireland by Thomas O'Neill Russell
  "https://www.gutenberg.org/cache/epub/30975/pg30975.txt", #Soil Culture by J. H. Walden
  "https://www.gutenberg.org/cache/epub/57320/pg57320.txt", #Telescopic Work for Starlight Evenings by William F. Denning
  "https://www.gutenberg.org/cache/epub/31006/pg31006.txt", #The Author's Printing and Publishing Assistant by Frederick Saunders
  "https://www.gutenberg.org/cache/epub/23476/pg23476.txt", #Churchwardens' Manual by George Henry Sumner
  "https://www.gutenberg.org/cache/epub/10733/pg10733.txt", #Studies in Civics by J. T. McCleary
  "https://www.gutenberg.org/cache/epub/57612/pg57612.txt", #Ladies' manual of art; or, profit and pastime. by Anonymous
  "https://www.gutenberg.org/cache/epub/29248/pg29248.txt", #The Young Lady's Equestrian Manual by Anonymous
  "https://www.gutenberg.org/cache/epub/60757/pg60757.txt", #Manual of Parliamentary Practice by Luther Stearns Cushing
  "https://www.gutenberg.org/cache/epub/62609/pg62609.txt", #Locomotive Engine Running and Management by Angus Sinclair
  "https://www.gutenberg.org/cache/epub/76936/pg76936.txt", #A practical guide for making post-mortem examinations : and for the study of…
  "https://www.gutenberg.org/cache/epub/63710/pg63710.txt", #A Manual of Photographic Chemistry, Including the Practice of the Collodion…
  "https://www.gutenberg.org/cache/epub/39044/pg39044.txt", #Advice to the people in general, with regard to their health by S. A. D. Tissot
  "https://www.gutenberg.org/cache/epub/49077/pg49077.txt", #The Art of Horse-Shoeing: A Manual for Farriers by William Hunting
  "https://www.gutenberg.org/cache/epub/38831/pg38831.txt", #The Barb and the Bridle by active 1866-1874 Robert Henderson
  "https://www.gutenberg.org/cache/epub/37142/pg37142.txt", #How to Care for the Insane: A Manual for Nurses by William D. Granger
  "https://www.gutenberg.org/cache/epub/44604/pg44604.txt", #How to become an engineer : containing full instructions how to proceed in…
  "https://www.gutenberg.org/cache/epub/74523/pg74523.txt", #A church dictionary by Walter Farquhar Hook
  "https://www.gutenberg.org/cache/epub/37309/pg37309.txt", #Violins and Violin Makers by Joseph Pearce
  "https://www.gutenberg.org/cache/epub/74485/pg74485.txt", #A handy dictionary of mythology : For everyday readers by Thomas Preston
  "https://www.gutenberg.org/cache/epub/44040/pg44040.txt", #Worcestershire in the Nineteenth Century by T. C. Turberville
  "https://www.gutenberg.org/cache/epub/67768/pg67768.txt", #Hand-book of Sanitary Information for Householders by Roger Sherman Tracy
  "https://www.gutenberg.org/cache/epub/64140/pg64140.txt", #Soup and Soup Making by Emma P. Ewing
  "https://www.gutenberg.org/cache/epub/78002/pg78002.txt", #The ladies' hand-book of millinery and dressmaking : With plain instructions…
  "https://www.gutenberg.org/cache/epub/66524/pg66524.txt", #The Wine Press and the Cellar: A Manual for the Wine-Maker and the Cellar-Man
  "https://www.gutenberg.org/cache/epub/58756/pg58756.txt", #A manual of pyrotechny : or, A familiar system of recreative fire-works
  "https://www.gutenberg.org/cache/epub/60550/pg60550.txt", #The Science of Brickmaking by George Frederick Harris
  "https://www.gutenberg.org/cache/epub/67942/pg67942.txt", #The honey bee: a manual of instruction in apiculture by Frank Benton
  "https://www.gutenberg.org/cache/epub/68157/pg68157.txt", #Manual of the apiary by Albert John Cook
  "https://www.gutenberg.org/cache/epub/32838/pg32838.txt", #The Canadian Curler's Manual by James Bicket
  "https://www.gutenberg.org/cache/epub/29701/pg29701.txt", #The Mother's Manual of Children's Diseases by Charles West
  "https://www.gutenberg.org/cache/epub/63517/pg63517.txt", #A Practical Manual of the Collodion Process, Giving in Detail a Method For…
  "https://www.gutenberg.org/cache/epub/71782/pg71782.txt", #Steel : a manual for steel users by William Metcalf
  "https://www.gutenberg.org/cache/epub/52850/pg52850.txt", #Barbers' Manual (Part 1); Text Book on Taxidermy (Part 2) by T. J. McConnaughay
  "https://www.gutenberg.org/cache/epub/76043/pg76043.txt", #Every woman her own flower gardener : A handy manual of flower gardening for…
  "https://www.gutenberg.org/cache/epub/62200/pg62200.txt", #Sabbath Defence Tactics: a manual by James Bridges
  "https://www.gutenberg.org/cache/epub/12942/pg12942.txt", #The Highland Fling and How to Teach it by Horatio N. Grant
  "https://www.gutenberg.org/cache/epub/67477/pg67477.txt", #Bee-keeping for the Many; or, The management of the common and Ligurian honey…
  "https://www.gutenberg.org/cache/epub/67439/pg67439.txt", #The Bee Keeper's Guide, Third Edition by J. H. Payne
  "https://www.gutenberg.org/cache/epub/57273/pg57273.txt", #The Stocking-Knitter's Manual: A Handy Book for the Work-Table by Cupples
  "https://www.gutenberg.org/cache/epub/73434/pg73434.txt", #Prof. E. H. Crane's manual of instructions to undertakers : With full and…
  "https://www.gutenberg.org/cache/epub/78603/pg78603.txt", #The harness makers' illustrated manual by William N. Fitz-Gerald
  ##### LARGER BOOKS/TEXTBOOKS #####
  "https://www.gutenberg.org/cache/epub/25717/pg25717.txt", #The History of the Decline and Fall of the Roman Empire by Edward Gibbon
  "https://www.gutenberg.org/cache/epub/2464/pg2464.txt",   #History of Florence and of the Affairs of Italy by Niccolò Machiavelli
  "https://www.gutenberg.org/cache/epub/25848/pg25848.txt", #William the Conqueror by Jacob Abbott
  "https://www.gutenberg.org/cache/epub/27551/pg27551.txt", #Hannibal by Jacob Abbott
  "https://www.gutenberg.org/cache/epub/26939/pg26939.txt", #Richard I by Jacob Abbott
  "https://www.gutenberg.org/cache/epub/26734/pg26734.txt", #Charles I by Jacob Abbott
  "https://www.gutenberg.org/cache/epub/27802/pg27802.txt", #Darius the Great by Jacob Abbott
  "https://www.gutenberg.org/cache/epub/28433/pg28433.txt", #Richard II by Jacob Abbott
  "https://www.gutenberg.org/cache/epub/25351/pg25351.txt", #Xerxes by Jacob Abbott
  "https://www.gutenberg.org/cache/epub/27240/pg27240.txt", #Pyrrhus by Jacob Abbott
  "https://www.gutenberg.org/cache/epub/28283/pg28283.txt", #Mary Queen of Scots by Jacob Abbott
  "https://www.gutenberg.org/cache/epub/15400/pg15400.txt", #Renaissance in Italy, Volume 1 (of 7) by John Addington Symonds
  "https://www.gutenberg.org/cache/epub/41924/pg41924.txt", #Renaissance in Italy, Volume 2 (of 7) by John Addington Symonds
  "https://www.gutenberg.org/cache/epub/11559/pg11559.txt", #Renaissance in Italy, Volume 3 (of 7) by John Addington Symonds
  "https://www.gutenberg.org/cache/epub/35792/pg35792.txt", #Renaissance in Italy, Volume 4 (of 7) by John Addington Symonds
  "https://www.gutenberg.org/cache/epub/36448/pg36448.txt", #Renaissance in Italy, Volume 5 (of 7) by John Addington Symonds
  "https://www.gutenberg.org/cache/epub/16504/pg16504.txt", #Renaissance in Italy, Volumes 6 and 7 (of 7) by John Addington Symonds
  "https://www.gutenberg.org/cache/epub/30624/pg30624.txt", #Alexander the Great by Jacob Abbott
  "https://www.gutenberg.org/cache/epub/28667/pg28667.txt", #Genghis Khan, Makers of History Series by Jacob Abbott
  "https://www.gutenberg.org/cache/epub/27692/pg27692.txt", #Romulus by Jacob Abbott
  "https://www.gutenberg.org/cache/epub/27312/pg27312.txt", #Nero by Jacob Abbott
  "https://www.gutenberg.org/cache/epub/28561/pg28561.txt", #Richard III by Jacob Abbott
  "https://www.gutenberg.org/cache/epub/40205/pg40205.txt", #History of Cleopatra, Queen of Egypt by Jacob Abbott
  "https://www.gutenberg.org/cache/epub/29107/pg29107.txt", #Queen Elizabeth by Jacob Abbott
  "https://www.gutenberg.org/cache/epub/10992/pg10992.txt", #Cleopatra by Jacob Abbott
  "https://www.gutenberg.org/cache/epub/16545/pg16545.txt", #King Alfred of England by Jacob Abbott
  "https://www.gutenberg.org/cache/epub/30707/pg30707.txt", #Cyrus the Great by Jacob Abbott
  "https://www.gutenberg.org/cache/epub/21889/pg21889.txt", #Peter the Great by Jacob Abbott
  "https://www.gutenberg.org/cache/epub/1972/pg1972.txt",   #History of the Britons (Historia Brittonum) by active 796 Nennius
  "https://www.gutenberg.org/cache/epub/61475/pg61475.txt", #Byzantine Constantinople, the walls of the city and adjoining historical sites
  "https://www.gutenberg.org/cache/epub/45815/pg45815.txt", #The Great Pestilence (A.D. 1348-9), Now Commonly Known as the Black Death
  "https://www.gutenberg.org/cache/epub/44308/pg44308.txt", #The Art of War in the Middle Ages A.D. 378-1515 by Charles Oman
  "https://www.gutenberg.org/cache/epub/42686/pg42686.txt", #A History of Epidemics in Britain, Volume 1 (of 2) by Charles Creighton
  "https://www.gutenberg.org/cache/epub/43671/pg43671.txt", #A History of Epidemics in Britain, Volume 2 (of 2) by Charles Creighton
  "https://www.gutenberg.org/cache/epub/28556/pg28556.txt", #History of Woman Suffrage, Volume III by Stanton, Anthony, and Gage
  "https://www.gutenberg.org/cache/epub/22305/pg22305.txt", #The Naval History of the United States. Volume 1 by Willis J. Abbot
  "https://www.gutenberg.org/cache/epub/26416/pg26416.txt", #The Naval History of the United States. Volume 2 by Willis J. Abbot
  "https://www.gutenberg.org/cache/epub/15735/pg15735.txt", #History of the Negro Race in America from 1619 to 1880. Vol 1 by Williams
  "https://www.gutenberg.org/cache/epub/21851/pg21851.txt", #History of the Negro Race in America from 1619 to 1880. Vol. 2 by Williams
  "https://www.gutenberg.org/cache/epub/21990/pg21990.txt", #The Campaign of 1776 around New York and Brooklyn by Henry Phelps Johnston
  "https://www.gutenberg.org/cache/epub/3072/pg3072.txt",   #Andersonville: A Story of Rebel Military Prisons by John McElroy
  "https://www.gutenberg.org/cache/epub/21012/pg21012.txt", #The loyalists of America and their times : from 1620 to 1816, Vol. 1 of 2
  "https://www.gutenberg.org/cache/epub/24658/pg24658.txt", #The loyalists of America and their times : from 1620 to 1816, Vol. 2 of 2
  "https://www.gutenberg.org/cache/epub/25119/pg25119.txt", #The Conquest of Canada, Vol. 1 by George Warburton
  "https://www.gutenberg.org/cache/epub/34862/pg34862.txt", #The Conquest of Canada, Vol. 2 by George Warburton
  "https://www.gutenberg.org/cache/epub/27430/pg27430.txt", #The Critical Period of American History by John Fiske
  "https://www.gutenberg.org/cache/epub/22131/pg22131.txt", #The Story of the Upper Canadian Rebellion, Volume 1 by John Charles Dent
  "https://www.gutenberg.org/cache/epub/15263/pg15263.txt", #The Underground Railroad by William Still
  "https://www.gutenberg.org/cache/epub/7142/pg7142.txt",   #The History of the Peloponnesian War by Thucydides
  "https://www.gutenberg.org/cache/epub/2707/pg2707.txt",   #The History of Herodotus — Volume 1 by Herodotus
  "https://www.gutenberg.org/cache/epub/2456/pg2456.txt",   #The History of Herodotus — Volume 2 by Herodotus
  "https://www.gutenberg.org/cache/epub/46976/pg46976.txt", #The Anabasis of Alexander : or, The history of the wars and conquests of…
  "https://www.gutenberg.org/cache/epub/2850/pg2850.txt",   #The Wars of the Jews; Or, The History of the Destruction of Jerusalem by Josephus
  "https://www.gutenberg.org/cache/epub/1170/pg1170.txt",   #Anabasis by Xenophon
  "https://www.gutenberg.org/cache/epub/6400/pg6400.txt",   #The Lives of the Twelve Caesars, Complete by Suetonius
  "https://www.gutenberg.org/cache/epub/27114/pg27114.txt", #Ancient States and Empires by John Lord
  "https://www.gutenberg.org/cache/epub/19725/pg19725.txt", #The History of Rome, Books 01 to 08 by Livy
  "https://www.gutenberg.org/cache/epub/10907/pg10907.txt", #The History of Rome, Books 09 to 26 by Livy
  "https://www.gutenberg.org/cache/epub/12582/pg12582.txt", #The History of Rome, Books 27 to 36 by Livy
  "https://www.gutenberg.org/cache/epub/44318/pg44318.txt", #The History of Rome, Books 37 to the End by Livy
  "https://www.gutenberg.org/cache/epub/1174/pg1174.txt",   #Hellenica by Xenophon
  "https://www.gutenberg.org/cache/epub/26390/pg26390.txt", #The Two Great Retreats of History by George Grote and comte de Philippe-Paul Ségur
  "https://www.gutenberg.org/cache/epub/16927/pg16927.txt", #Tacitus: The Histories, Volumes I and II by Cornelius Tacitus
  "https://www.gutenberg.org/cache/epub/57374/pg57374.txt", #Annals and Antiquities of Rajasthan, v. 1 of 3 by James Tod
  "https://www.gutenberg.org/cache/epub/57375/pg57375.txt", #Annals and Antiquities of Rajasthan, v. 2 of 3 by James Tod
  "https://www.gutenberg.org/cache/epub/57376/pg57376.txt", #Annals and Antiquities of Rajasthan, v. 3 of 3 by James Tod
  "https://www.gutenberg.org/cache/epub/2124/pg2124.txt",   #A Record of Buddhistic Kingdoms by Faxian
  "https://www.gutenberg.org/cache/epub/49403/pg49403.txt", #The Seri Indians. (1898 N 17 / 1895-1896 (pages 1-344*)) by W J McGee
  "https://www.gutenberg.org/cache/epub/23224/pg23224.txt", #Historical Introduction to Studies Among the Sedentary Indians of New Mexico;…
  "https://www.gutenberg.org/cache/epub/20218/pg20218.txt", #History of the Incas by Pedro Sarmiento de Gamboa
  "https://www.gutenberg.org/cache/epub/37887/pg37887.txt", #Mexico, Aztec, Spanish and Republican, Vol. 1 of 2 by Brantz Mayer
  "https://www.gutenberg.org/cache/epub/49538/pg49538.txt", #Mexico, Aztec, Spanish and Republican, Vol. 2 of 2 by Brantz Mayer
  "https://www.gutenberg.org/cache/epub/1301/pg1301.txt",   #The French Revolution: A History by Thomas Carlyle
  "https://www.gutenberg.org/cache/epub/17450/pg17450.txt", #The Part Borne by the Dutch in the Discovery of Australia 1606-1765 by J. E. Heeres
  "https://www.gutenberg.org/cache/epub/22762/pg22762.txt", #History of the Rise of the Huguenots, Vol. 1 by Henry Martyn Baird
  "https://www.gutenberg.org/cache/epub/30708/pg30708.txt", #History of the Rise of the Huguenots, Vol. 2 by Henry Martyn Baird
  "https://www.gutenberg.org/cache/epub/16764/pg16764.txt", #History of the Wars, Books I and II: The Persian War by Procopius
  "https://www.gutenberg.org/cache/epub/16765/pg16765.txt", #History of the Wars, Books III and IV: The Vandalic War by Procopius
  "https://www.gutenberg.org/cache/epub/20298/pg20298.txt", #History of the Wars, Books V and VI: The Gothic War by Procopius
  "https://www.gutenberg.org/cache/epub/17037/pg17037.txt", #History of the English People, Volume I by John Richard Green
  "https://www.gutenberg.org/cache/epub/17038/pg17038.txt", #History of the English People, Volume II by John Richard Green
  "https://www.gutenberg.org/cache/epub/20812/pg20812.txt", #History of the English People, Volume III by John Richard Green
  "https://www.gutenberg.org/cache/epub/23317/pg23317.txt", #History of the English People, Volume IV by John Richard Green
  "https://www.gutenberg.org/cache/epub/23642/pg23642.txt", #History of the English People, Volume V by John Richard Green
  "https://www.gutenberg.org/cache/epub/24254/pg24254.txt", #History of the English People, Volume VI by John Richard Green
  "https://www.gutenberg.org/cache/epub/25261/pg25261.txt", #History of the English People, Volume VII by John Richard Green
  "https://www.gutenberg.org/cache/epub/25536/pg25536.txt", #History of the English People, Volume VIII by John Richard Green
  "https://www.gutenberg.org/cache/epub/33504/pg33504.txt", #Opticks : or, A treatise of the reflections, refractions, inflections and…
  "https://www.gutenberg.org/cache/epub/22062/pg22062.txt", #The Mathematicall Praeface to Elements of Geometrie of Euclid of Megara by John Dee
  "https://www.gutenberg.org/cache/epub/26752/pg26752.txt", #The Way To Geometry by Petrus Ramus
  "https://www.gutenberg.org/cache/epub/21076/pg21076.txt", #The First Six Books of the Elements of Euclid by Euclid and John Casey
  "https://www.gutenberg.org/cache/epub/68662/pg68662.txt", #Elements of arithmetic by Augustus De Morgan
  "https://www.gutenberg.org/cache/epub/5000/pg5000.txt",   #The Notebooks of Leonardo Da Vinci — Complete by da Vinci Leonardo
  "https://www.gutenberg.org/cache/epub/50572/pg50572.txt", #Goethe's Theory of Colours by Johann Wolfgang von Goethe
  "https://www.gutenberg.org/cache/epub/14986/pg14986.txt", #Experimental Researches in Electricity, Volume 1 by Michael Faraday
  "https://www.gutenberg.org/cache/epub/46036/pg46036.txt", #The sidereal messenger of Galileo Galilei : and a part of the preface to…
  "https://www.gutenberg.org/cache/epub/37729/pg37729.txt", #A Discourse Presented to the Most Serene Don Cosimo II., Great Duke of Tuscany,…
  "https://www.gutenberg.org/cache/epub/13476/pg13476.txt", #Experiments with Alternate Currents of High Potential and High Frequency by Tesla
  "https://www.gutenberg.org/cache/epub/33810/pg33810.txt", #On the magnet, magnetick bodies also, and on the great magnet the earth by Gilbert et al.
  "https://www.gutenberg.org/cache/epub/41839/pg41839.txt", #The Boy's Playbook of Science by John Henry Pepper
  "https://www.gutenberg.org/cache/epub/45515/pg45515.txt", #Experiments and Observations on Electricity Made at Philadelphia in America
  "https://www.gutenberg.org/cache/epub/54969/pg54969.txt", #Sound by John Tyndall
  "https://www.gutenberg.org/cache/epub/63803/pg63803.txt", #The Forms of Water in Clouds and Rivers, Ice and Glaciers by John Tyndall
  "https://www.gutenberg.org/cache/epub/52869/pg52869.txt", #On the Connexion of the Physical Sciences by Mary Somerville
  "https://www.gutenberg.org/cache/epub/55886/pg55886.txt", #On Molecular and Microscopic Science, Volume 1 (of 2) by Mary Somerville
  "https://www.gutenberg.org/cache/epub/57566/pg57566.txt", #On Molecular and Microscopic Science, Volume 2 (of 2) by Mary Somerville
  "https://www.gutenberg.org/cache/epub/71191/pg71191.txt", #The celestial worlds discover'd : or, conjectures concerning the inhabitants,…
  "https://www.gutenberg.org/cache/epub/30775/pg30775.txt", #Elements of Chemistry, by Antoine Laurent Lavoisier
  "https://www.gutenberg.org/cache/epub/51326/pg51326.txt", #The Principles of Chemistry, Volume I by Dmitry Ivanovich Mendeleyev
  "https://www.gutenberg.org/cache/epub/54210/pg54210.txt", #The Principles of Chemistry, Volume II by Dmitry Ivanovich Mendeleyev
  "https://www.gutenberg.org/cache/epub/74240/pg74240.txt", #The works of the highly experienced and famous chymist, John Rudolph Glauber…
  "https://www.gutenberg.org/cache/epub/63355/pg63355.txt", #Studies on fermentation : the diseases of beer, their causes, and the means of…
  "https://www.gutenberg.org/cache/epub/29734/pg29734.txt", #Experiments and Observations on Different Kinds of Air by Joseph Priestley
  "https://www.gutenberg.org/cache/epub/37682/pg37682.txt", #Heads of Lectures on a Course of Experimental Philosophy: Particularly…
  "https://www.gutenberg.org/cache/epub/61112/pg61112.txt", #A New Light of Alchymie by Michal Sedziwój and Paracelsus
  "https://www.gutenberg.org/cache/epub/46998/pg46998.txt", #Elements of the Theory and Practice of Chymistry, 5th ed. by Pierre Joseph Macquer
  "https://www.gutenberg.org/cache/epub/58393/pg58393.txt", #The Mirror of Alchimy by Roger Bacon
  "https://www.gutenberg.org/cache/epub/1228/pg1228.txt",   #On the Origin of Species By Means of Natural Selection by Charles Darwin
  "https://www.gutenberg.org/cache/epub/2300/pg2300.txt",   #The Descent of Man, and Selection in Relation to Sex by Charles Darwin
  "https://www.gutenberg.org/cache/epub/24923/pg24923.txt", #The Variation of Animals and Plants Under Domestication, Vol. I. by Charles Darwin
  "https://www.gutenberg.org/cache/epub/1227/pg1227.txt",   #The Expression of the Emotions in Man and Animals by Charles Darwin
  "https://www.gutenberg.org/cache/epub/22728/pg22728.txt", #The Foundations of the Origin of Species by Charles Darwin
  "https://www.gutenberg.org/cache/epub/2355/pg2355.txt",   #The Formation of Vegetable Mould Through the Action of Worms by Charles Darwin
  "https://www.gutenberg.org/cache/epub/28897/pg28897.txt", #The Variation of Animals and Plants Under Domestication, Volume II (of 2) by Darwin

  

]
