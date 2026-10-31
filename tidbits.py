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

]
