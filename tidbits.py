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

]
