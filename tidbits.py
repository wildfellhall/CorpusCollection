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
  "https://www.gutenberg.org/cache/epub/57493/pg74739.txt", #A military dictionary : or, Explanation of the several systems of discipline…
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

]
