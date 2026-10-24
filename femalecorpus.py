"""
Still undergoing expansion processes. My first checkpoint in terms of length will be 300 books, but a length closer to 500 books would be ideal. 
"""
sources = [
    "https://www.gutenberg.org/files/1342/1342-0.txt",   #Pride and Prejudice by Jane Austen
    "https://www.gutenberg.org/files/3268/3268-0.txt",   #The Mysteries of Udolpho by Ann Ward Radcliffe
    "https://www.gutenberg.org/files/21839/21839-0.txt", #Sense and Sensibility by Jane Austen
    "https://www.gutenberg.org/files/121/121-0.txt",     #Northanger Abbey by Jane Austen
    "https://www.gutenberg.org/files/158/158-0.txt",     #Emma by Jane Austen
    "https://www.gutenberg.org/files/105/105-0.txt",     #Persuasion by Jane Austen
    "https://www.gutenberg.org/files/141/141-0.txt",     #Mansfield Park by Jane Austen
    "https://www.gutenberg.org/files/145/145-0.txt",     #Middlemarch by George Eliot
    "https://www.gutenberg.org/files/550/550-0.txt",     #Silas Marner by George Eliot
    "https://www.gutenberg.org/files/507/507-0.txt",     #Adam Bede by George Eliot
    "https://www.gutenberg.org/files/6688/6688-0.txt",   #The Mill on the Floss by George Eliot
    "https://www.gutenberg.org/files/7469/7469-0.txt",   #Daniel Deronda by George Eliot
    "https://www.gutenberg.org/files/24020/24020-0.txt", #Romola by George Eliot
    "https://www.gutenberg.org/files/969/969-0.txt",     #The Tenant of Wildfell Hall by Anne Brontë
    "https://www.gutenberg.org/files/767/767-0.txt",     #Agnes Grey by Anne Brontë
    "https://www.gutenberg.org/files/1028/1028-0.txt",   #The Professor by Charlotte Brontë
    "https://www.gutenberg.org/files/30486/30486-0.txt", #Shirley by Charlotte Brontë
    "https://www.gutenberg.org/files/9182/9182-0.txt",   #Villette by Charlotte Brontë
    "https://www.gutenberg.org/files/1260/1260-0.txt",   #Jane Eyre: An Autobiography by Charlotte Brontë
    "https://www.gutenberg.org/files/768/768-0.txt",     #Wuthering Heights by Emily Brontë
    "https://www.gutenberg.org/files/37106/37106-0.txt", #Little Women; Or, Meg, Jo, Beth, and Amy by Louisa May Alcott
    "https://www.gutenberg.org/files/28203/28203-0.txt", #Moods by Louisa May Alcott
    "https://www.gutenberg.org/files/41127/41127-0.txt", #Rose in Bloom by Louisa May Alcott
    "https://www.gutenberg.org/files/2787/2787-0.txt",   #An Old-Fashioned Girl by Louisa May Alcott
    "https://www.gutenberg.org/files/2726/2726-0.txt",   #Eight Cousins by Louisa May Alcott
    "https://www.gutenberg.org/files/2786/2786-0.txt",   #Jack and Jill by Louisa May Alcott
    "https://www.gutenberg.org/files/2788/2788-0.txt",   #Little Men: Life at Plumfield With Jo's Boys by Louisa May Alcott
    "https://www.gutenberg.org/files/3499/3499-0.txt",   #Jo's Boys by Louisa May Alcott
    "https://www.gutenberg.org/files/84/84-0.txt",       #Frankenstein; or, the modern prometheus by Mary Wollstonecraft Shelley
    "https://www.gutenberg.org/files/18247/18247-0.txt", #The Last Man by Mary Wollstonecraft Shelley
    "https://www.gutenberg.org/files/15238/15238-0.txt", #Mathilda by Mary Wollstonecraft Shelley
    "https://www.gutenberg.org/files/64329/64329-0.txt", #Falkner: A Novel by Mary Wollstonecraft Shelley
    "https://www.gutenberg.org/files/394/394-0.txt",     #Cranford by Elizabeth Cleghorn Gaskell
    "https://www.gutenberg.org/files/4276/4276-0.txt",   #North and South by Elizabeth Cleghorn Gaskell
    "https://www.gutenberg.org/files/2153/2153-0.txt",   #Mary Barton by Elizabeth Cleghorn Gaskell
    "https://www.gutenberg.org/files/4274/4274-0.txt",   #Wives and Daughters by Elizabeth Cleghorn Gaskell
    "https://www.gutenberg.org/files/4275/4275-0.txt",   #Ruth by Elizabeth Cleghorn Gaskell
    "https://www.gutenberg.org/files/2524/2524-0.txt",   #My Lady Ludlow by Elizabeth Cleghorn Gaskell
    "https://www.gutenberg.org/files/4537/4537-0.txt",   #Sylvia's Lovers — Complete by Elizabeth Cleghorn Gaskell
    "https://www.gutenberg.org/files/4268/4268-0.txt",   #Cousin Phillis by Elizabeth Cleghorn Gaskell
    "https://www.gutenberg.org/files/2522/2522-0.txt",   #A Dark Night's Work by Elizabeth Cleghorn Gaskell
    "https://www.gutenberg.org/files/7371/7371-0.txt",   #A Sicilian Romance by Ann Ward Radcliffe
    "https://www.gutenberg.org/files/64701/64701-0.txt", #The Romance of the Forest, interspersed with some pieces of poetry. by Radcliffe
    "https://www.gutenberg.org/files/66545/66545-0.txt", #The Heir of Mondolfo by Mary Wollstonecraft Shelley
    "https://www.gutenberg.org/files/31180/31180-0.txt", #Ellen Middleton—A Tale by Georgiana Fullerton
    "https://www.gutenberg.org/files/3322/3322-0.txt",   #East Lynne by Mrs. Henry Wood
    "https://www.gutenberg.org/files/15627/15627-0.txt", #Verner's Pride by Mrs. Henry Wood
    "https://www.gutenberg.org/files/34587/34587-0.txt", #Mrs. Halliburton's Troubles by Mrs. Henry Wood
    "https://www.gutenberg.org/files/22121/22121-0.txt", #Olive: A Novel by Dinah Maria Mulock Craik
    "https://www.gutenberg.org/files/45975/45975-0.txt", #The Little Lame Prince and His Travelling Cloak by Dinah Maria Mulock Craik
    "https://www.gutenberg.org/files/21767/21767-0.txt", #Agatha's Husband: A Novel by Dinah Maria Mulock Craik
    "https://www.gutenberg.org/files/2351/2351-0.txt",   #John Halifax, Gentleman by Dinah Maria Mulock Craik
    "https://www.gutenberg.org/files/13461/13461-0.txt", #Mistress and Maid: A Household Story by Dinah Maria Mulock Craik
    "https://www.gutenberg.org/files/14708/14708-0.txt", #The Laurel Bush: An Old-Fashioned Love Story by Dinah Maria Mulock Craik
    "https://www.gutenberg.org/files/36157/36157-0.txt", #Daisy Burns (Volume 1) by Julia Kavanagh
    "https://www.gutenberg.org/files/36158/36158-0.txt", #Daisy Burns (Volume 2) by Julia Kavanagh
    "https://www.gutenberg.org/files/36160/36160-0.txt", #Rachel Gray: A Tale Founded on Fact by Julia Kavanagh
    "https://www.gutenberg.org/files/1952/1952-0.txt",   #The Yellow Wallpaper by Charlotte Perkins Gilman
    "https://www.gutenberg.org/files/3016/3016-0.txt",   #What Diantha Did by Charlotte Perkins Gilman
    "https://www.gutenberg.org/files/6053/6053-0.txt",   #Evelina, Or, the History of a Young Lady's Entrance into the World by Fanny Burney
    "https://www.gutenberg.org/files/40619/40619-0.txt", #Camilla; or, A Picture of Youth by Fanny Burney
    "https://www.gutenberg.org/files/171/171-0.txt",     #Charlotte Temple by Mrs. Rowson
    "https://www.gutenberg.org/files/5182/5182-0.txt",   #The Old English Baron: a Gothic Story by Clara Reeve
    "https://www.gutenberg.org/files/23810/23810-0.txt", #At Fault by Kate Chopin
    "https://www.gutenberg.org/files/6346/6346-0.txt",   #Cecilia; Or, Memoirs of an Heiress — Volume 1 by Fanny Burney
    "https://www.gutenberg.org/files/7146/7146-0.txt",   #Cecilia; Or, Memoirs of an Heiress — Volume 2 by Fanny Burney
    "https://www.gutenberg.org/files/7152/7152-0.txt",   #Cecilia; Or, Memoirs of an Heiress — Volume 3 by Fanny Burney
    "https://www.gutenberg.org/files/37437/37437-0.txt", #The Wanderer; or, Female Difficulties (Volume 1 of 5) by Fanny Burney
    "https://www.gutenberg.org/files/37438/37438-0.txt", #The Wanderer; or, Female Difficulties (Volume 2 of 5) by Fanny Burney
    "https://www.gutenberg.org/files/37439/37439-0.txt", #The Wanderer; or, Female Difficulties (Volume 3 of 5) by Fanny Burney
    "https://www.gutenberg.org/files/37440/37440-0.txt", #The Wanderer; or, Female Difficulties (Volume 4 of 5) by Fanny Burney
    "https://www.gutenberg.org/files/37441/37441-0.txt", #The Wanderer; or, Female Difficulties (Volume 5 of 5) by Fanny Burney
    "https://www.gutenberg.org/files/40882/40882-0.txt", #Felix Holt, the Radical by George Eliot
    "https://www.gutenberg.org/files/2165/2165-0.txt",   #The Lifted Veil by George Eliot
    "https://www.gutenberg.org/files/2171/2171-0.txt",   #Brother Jacob by George Eliot
    "https://www.gutenberg.org/files/10762/10762-0.txt", #Impressions of Theophrastus Such by George Eliot
    "https://www.gutenberg.org/files/2547/2547-0.txt",   #Half a Life-Time Ago by Elizabeth Cleghorn Gaskell
    "https://www.gutenberg.org/files/11371/11371-0.txt", #The Moorland Cottage by Elizabeth Cleghorn Gaskell
    "https://www.gutenberg.org/files/2549/2549-0.txt",   #The Doom of the Griffiths by Elizabeth Cleghorn Gaskell
    "https://www.gutenberg.org/files/50054/50054-0.txt", #The Female Quixote; or, The Adventures of Arabella, v. 1-2 by Charlotte Lennox
    "https://www.gutenberg.org/files/45187/45187-0.txt", #The Household of Sir Thomas More by Anne Manning
    "https://www.gutenberg.org/files/61080/61080-0.txt", #Cherry & Violet: A Tale of the Great Plague by Anne Manning
    "https://www.gutenberg.org/files/51829/51829-0.txt", #The Old Chelsea Bun-House: A Tale of the Last Century by Anne Manning
    "https://www.gutenberg.org/files/49290/49290-0.txt", #The Year Nine: A Tale of the Tyrol by Anne Manning
    "https://www.gutenberg.org/files/42296/42296-0.txt", #The Duchess of Trajetto by Anne Manning
    "https://www.gutenberg.org/files/67612/67612-0.txt", #Love in Excess; or, the Fatal Enquiry by Eliza Fowler Haywood
    "https://www.gutenberg.org/files/46346/46346-0.txt", #The History of Miss Betsy Thoughtless by Eliza Fowler Haywood
    "https://www.gutenberg.org/files/10804/10804-0.txt", #The Fortunate Foundlings by Eliza Fowler Haywood
    "https://www.gutenberg.org/files/15455/15455-0.txt", #Life's Progress Through the Passions; Or, The Adventures of Natura by Haywood
    "https://www.gutenberg.org/files/1424/1424-0.txt",   #Castle Rackrent by Maria Edgeworth
    "https://www.gutenberg.org/files/1473/1473-0.txt",   #The Absentee by Maria Edgeworth
    "https://www.gutenberg.org/files/271/271-0.txt",     #Black Beauty : The autobiography of a horse by Anna Sewell
    "https://www.gutenberg.org/files/479/479-0.txt",     #Little Lord Fauntleroy by Frances Hodgson Burnett
    "https://www.gutenberg.org/files/25810/25810-0.txt", #In Connection with the De Willoughby Claim by Frances Hodgson Burnett
    "https://www.gutenberg.org/files/137/137-0.txt",     #Sara Crewe; Or, What Happened at Miss Minchin's Boarding School by Burnett
    "https://www.gutenberg.org/files/35300/35300-0.txt", #Louisiana by Frances Hodgson Burnett
    "https://www.gutenberg.org/files/15651/15651-0.txt", #His Grace of Osmonde by Frances Hodgson Burnett
    "https://www.gutenberg.org/files/1550/1550-0.txt",   #A Lady of Quality by Frances Hodgson Burnett
    "https://www.gutenberg.org/files/9487/9487-0.txt",   #A Fair Barbarian by Frances Hodgson Burnett
    "https://www.gutenberg.org/files/25726/25726-0.txt", #The pretty sister of José by Frances Hodgson Burnett
    "https://www.gutenberg.org/files/25725/25725-0.txt", #That Lass O' Lowrie's by Frances Hodgson Burnett
    "https://www.gutenberg.org/files/25727/25727-0.txt", #Vagabondia by Frances Hodgson Burnett
    "https://www.gutenberg.org/files/1212/1212-0.txt",   #Love and Freindship [sic] by Jane Austen
    "https://www.gutenberg.org/files/2521/2521-0.txt",   #Lizzie Leigh by Elizabeth Cleghorn Gaskell
    "https://www.gutenberg.org/files/2548/2548-0.txt",   #The Poor Clare by Elizabeth Cleghorn Gaskell
    "https://www.gutenberg.org/files/17780/17780-0.txt", #Scenes of Clerical Life by George Eliot
    "https://www.gutenberg.org/files/30273/30273-0.txt", #Tom and Maggie Tulliver by George Eliot
    "https://www.gutenberg.org/files/74643/74643-0.txt", #The Italian, Volume 1 (of 3) : or, the confessional of the Black Penitents
    "https://www.gutenberg.org/files/74640/74640-0.txt", #The Italian, Volume 2 (of 3) : or, the confessional of the Black Penitents
    "https://www.gutenberg.org/files/66749/66749-0.txt", #The Fortunes of Perkin Warbeck: a romance by Mary Wollstonecraft Shelley
    "https://www.gutenberg.org/files/63337/63337-0.txt", #Valperga Volume 1 (of 3) by Mary Wollstonecraft Shelley
    "https://www.gutenberg.org/files/63338/63338-0.txt", #Valperga Volume 2 (of 3) by Mary Wollstonecraft Shelley
    "https://www.gutenberg.org/files/63339/63339-0.txt", #Valperga Volume 3 (of 3) by Mary Wollstonecraft Shelley
    "https://www.gutenberg.org/files/64555/64555-0.txt", #Lodore, Vol. 1 (of 3) by Mary Wollstonecraft Shelley
    "https://www.gutenberg.org/files/64556/64556-0.txt", #Lodore, Vol. 2 (of 3) by Mary Wollstonecraft Shelley
    "https://www.gutenberg.org/files/64557/64557-0.txt", #Lodore, Vol. 3 (of 3) by Mary Wollstonecraft Shelley
    "https://www.gutenberg.org/files/35638/35638-0.txt", #Leonora by Maria Edgeworth
    "https://www.gutenberg.org/files/2129/2129-0.txt",   #Murad the Unlucky, and Other Tales by Maria Edgeworth
    "https://www.gutenberg.org/files/62219/62219-0.txt", #The Day of Small Things by Anne Manning
    "https://www.gutenberg.org/files/51557/51557-0.txt", #The Colloquies of Edward Osborne, Citizen and Clothworker of London by Anne Manning
    "https://www.gutenberg.org/files/35548/35548-0.txt", #Doctor Cupid: A Novel by Rhoda Broughton
    "https://www.gutenberg.org/files/12304/12304-0.txt", #Nancy: A Novel by Rhoda Broughton
    "https://www.gutenberg.org/files/45178/45178-0.txt", #Red as a Rose is She: A Novel by Rhoda Broughton
    "https://www.gutenberg.org/files/34428/34428-0.txt", #Alas! A Novel by Rhoda Broughton
    "https://www.gutenberg.org/files/18459/18459-0.txt", #Dainty's Cruel Rivals; Or, The Fatal Birthday by Mrs. Alex. McVeigh Miller
    "https://www.gutenberg.org/files/7184/7184-0.txt",   #A Heart-Song of To-day (Disturbed by Fire from the 'Unruly Member'): A Novel
    "https://www.gutenberg.org/files/23789/23789-0.txt", #Cruel as the grave by Emma Dorothy Eliza Nevitte Southworth
    "https://www.gutenberg.org/files/42283/42283-0.txt", #The San Rosario Ranch by Maud Howe Elliott
    "https://www.gutenberg.org/files/3823/3823-0.txt",   #Thelma by Marie Corelli
    "https://www.gutenberg.org/files/42332/42332-0.txt", #The Sorrows of Satan by Marie Corelli
    "https://www.gutenberg.org/files/4360/4360-0.txt",   #Vendetta: A Story of One Forgotten by Marie Corelli
    "https://www.gutenberg.org/files/4394/4394-0.txt",   #A Romance of Two Worlds: A Novel by Marie Corelli
    "https://www.gutenberg.org/files/53097/53097-0.txt", #The Murder of Delicia by Marie Corelli
    "https://www.gutenberg.org/files/5114/5114-0.txt",   #Ardath: The Story of a Dead Self by Marie Corelli
    "https://www.gutenberg.org/files/68771/68771-0.txt", #The soul of Lilith by Marie Corelli
    "https://www.gutenberg.org/files/5079/5079-0.txt",   #Ziska: The Problem of a Wicked Soul by Marie Corelli
    "https://www.gutenberg.org/files/49806/49806-0.txt", #Addie's Husband; or, Through clouds to sunshine by Mrs. Gordon Smythies
    "https://www.gutenberg.org/files/36360/36360-0.txt", #Faithful Margaret: A Novel by Mrs. J. M. Simpson
    "https://www.gutenberg.org/files/76634/76634-0.txt", #Lillian's vow : or, The mystery of Raleigh House by Mrs. E. Burke Collins
    "https://www.gutenberg.org/files/76981/76981-0.txt", #Saved from herself : or, On the edge of doom by Adelaide Stirling
    "https://www.gutenberg.org/files/26259/26259-0.txt", #Her mother's secret by Emma Dorothy Eliza Nevitte Southworth
    "https://www.gutenberg.org/files/15774/15774-0.txt", #Ishmael; Or, In the Depths by Emma Dorothy Eliza Nevitte Southworth
    "https://www.gutenberg.org/files/29866/29866-0.txt", #Hidden hand by Emma Dorothy Eliza Nevitte Southworth
    "https://www.gutenberg.org/files/76591/76591-0.txt", #The deserted wife by Emma Dorothy Eliza Nevitte Southworth
    "https://www.gutenberg.org/files/29729/29729-0.txt", #Victor's Triumph by Emma Dorothy Eliza Nevitte Southworth
    "https://www.gutenberg.org/files/16094/16094-0.txt", #For Woman's Love by Emma Dorothy Eliza Nevitte Southworth
    "https://www.gutenberg.org/files/69828/69828-0.txt", #The bride's fate by Emma Dorothy Eliza Nevitte Southworth
    "https://www.gutenberg.org/files/3792/3792-0.txt",   #Capitola the madcap by Emma Dorothy Eliza Nevitte Southworth
    "https://www.gutenberg.org/files/16039/16039-0.txt", #The Lost Lady of Lone by Emma Dorothy Eliza Nevitte Southworth
    "https://www.gutenberg.org/files/75497/75497-0.txt", #The Lady of the Isle : or, the Island Princess by Southworth
    "https://www.gutenberg.org/files/69714/69714-0.txt", #The discarded daughter; or, The children of the isle by Southworth
    "https://www.gutenberg.org/files/70811/70811-0.txt", #Gloria : A novel by Emma Dorothy Eliza Nevitte Southworth
    "https://www.gutenberg.org/files/36713/36713-0.txt", #The Haunted Homestead: A Novel by Emma Dorothy Eliza Nevitte Southworth
    "https://www.gutenberg.org/files/69809/69809-0.txt", #For whose sake? by Emma Dorothy Eliza Nevitte Southworth
    "https://www.gutenberg.org/files/68610/68610-0.txt", #Love's labor won by Emma Dorothy Eliza Nevitte Southworth
    "https://www.gutenberg.org/files/70131/70131-0.txt", #How he won her by Emma Dorothy Eliza Nevitte Southworth
    "https://www.gutenberg.org/files/24337/24337-0.txt", #Capitola's peril by Emma Dorothy Eliza Nevitte Southworth
    "https://www.gutenberg.org/files/71098/71098-0.txt", #Dorothy Harcourt's secret : Sequel to "A deed without a name" by Southworth
    "https://www.gutenberg.org/files/70476/70476-0.txt", #India : the pearl of Pearl River by Emma Dorothy Eliza Nevitte Southworth
    "https://www.gutenberg.org/files/70855/70855-0.txt", #Lilith : A novel by Emma Dorothy Eliza Nevitte Southworth
    "https://www.gutenberg.org/files/70776/70776-0.txt", #The curse of Clifton : or, the widowed bride by Southworth
    "https://www.gutenberg.org/files/68273/68273-0.txt", #Love's bitterest cup by Emma Dorothy Eliza Nevitte Southworth
    "https://www.gutenberg.org/files/32757/32757-0.txt", #Tried for Her Life by Emma Dorothy Eliza Nevitte Southworth
    "https://www.gutenberg.org/files/14382/14382-0.txt", #The Missing Bride by Emma Dorothy Eliza Nevitte Southworth
    "https://www.gutenberg.org/files/69675/69675-0.txt", #Allworth Abbey by Emma Dorothy Eliza Nevitte Southworth
    "https://www.gutenberg.org/files/75006/75006-0.txt", #Fair play : a novel by Emma Dorothy Eliza Nevitte Southworth
    "https://www.gutenberg.org/files/69972/69972-0.txt", #The changed brides by Emma Dorothy Eliza Nevitte Southworth
    "https://www.gutenberg.org/files/6376/6376-0.txt",   #Self-Raised; Or, From the Depths by Emma Dorothy Eliza Nevitte Southworth
    "https://www.gutenberg.org/files/75317/75317-0.txt", #When shadows die by Emma Dorothy Eliza Nevitte Southworth
    "https://www.gutenberg.org/files/76916/76916-0.txt", #Em's husband : A sequel to "Em" by Emma Dorothy Eliza Nevitte Southworth
    "https://www.gutenberg.org/files/77295/77295-0.txt", #Brandon Coyle's wife : a sequel to "A skeleton in the closet" by Southworth
    "https://www.gutenberg.org/files/79290/79290-0.txt", #The fatal marriage : or, Orville Deville by Emma Dorothy Eliza Nevitte Southworth
    "https://www.gutenberg.org/files/22047/22047-0.txt", #The Love Affairs of an Old Maid by Lilian Bell
    "https://www.gutenberg.org/files/41646/41646-0.txt", #Emmeline, the Orphan of the Castle by Charlotte Smith
    "https://www.gutenberg.org/files/2601/2601-0.txt",   #Heartsease; Or, The Brother's Wife by Charlotte M. Yonge
    "https://www.gutenberg.org/files/5700/5700-0.txt",   #Love and Life: An Old Story in Eighteenth Century Costume by Charlotte M. Yonge
    "https://www.gutenberg.org/files/6006/6006-0.txt",   #Under the Storm by Charlotte M. Yonge
    "https://www.gutenberg.org/files/3610/3610-0.txt",   #The Daisy Chain, or Aspirations by Charlotte M. Yonge
    "https://www.gutenberg.org/files/2505/2505-0.txt",   #The Heir of Redclyffe by Charlotte M. Yonge
    "https://www.gutenberg.org/files/3292/3292-0.txt",   #The Clever Woman of the Family by Charlotte M. Yonge
    "https://www.gutenberg.org/files/3048/3048-0.txt",   #The Little Duke: Richard the Fearless by Charlotte M. Yonge
    "https://www.gutenberg.org/files/5080/5080-0.txt",   #Magnum Bonum; Or, Mother Carey's Brood by Charlotte M. Yonge
    "https://www.gutenberg.org/files/26156/26156-0.txt", #Hopes and Fears by Charlotte M. Yonge
    "https://www.gutenberg.org/files/203/203-0.txt",     #Uncle Tom's Cabin by Harriet Beecher Stowe
    "https://www.gutenberg.org/files/12354/12354-0.txt", #Pink and White Tyranny by Harriet Beecher Stowe
    "https://www.gutenberg.org/files/55012/55012-0.txt", #Dred: A Tale of the Great Dismal Swamp by Harriet Beecher Stowe
    "https://www.gutenberg.org/files/47874/47874-0.txt", #My Wife and I; Or, Harry Henderson's History by Harriet Beecher Stowe
    "https://www.gutenberg.org/files/31522/31522-0.txt", #The Pearl of Orr's Island: A Story of the Coast of Maine by Harriet Beecher Stowe
    "https://www.gutenberg.org/files/47958/47958-0.txt", #The Minister's Wooing by Harriet Beecher Stowe
    "https://www.gutenberg.org/files/43076/43076-0.txt", #Agnes of Sorrento by Harriet Beecher Stowe
    "https://www.gutenberg.org/files/48603/48603-0.txt", #We and Our Neighbors; or, The Records of an Unfashionable Street by Stowe
    "https://www.gutenberg.org/files/45415/45415-0.txt", #The Chimney-Corner by Harriet Beecher Stowe
    "https://www.gutenberg.org/files/67383/67383-0.txt", #Little Foxes by Harriet Beecher Stowe
    "https://www.gutenberg.org/files/48190/48190-0.txt", #Poganuc People: Their Loves and Lives by Harriet Beecher Stowe
    "https://www.gutenberg.org/files/5843/5843-0.txt",   #The Young Step-Mother; Or, A Chronicle of Mistakes by Charlotte M. Yonge
    "https://www.gutenberg.org/files/6331/6331-0.txt",   #The Pillars of the House; Or, Under Wode, Under Rode, Vol. 1 (of 2) by Yonge
    "https://www.gutenberg.org/files/5124/5124-0.txt",   #Henrietta's Wish; Or, Domineering by Charlotte M. Yonge
    "https://www.gutenberg.org/files/44721/44721-0.txt", #The Pillars of the House; Or, Under Wode, Under Rode, Vol. 2 (of 2) by Yonge
    "https://www.gutenberg.org/files/5274/5274-0.txt",   #The Chaplet of Pearls by Charlotte M. Yonge
    "https://www.gutenberg.org/files/4235/4235-0.txt",   #Dynevor Terrace; Or, The Clue of Life — Volume 1 by Charlotte M. Yonge
    "https://www.gutenberg.org/files/3744/3744-0.txt",   #The Trial; Or, More Links of the Daisy Chain by Charlotte M. Yonge
    "https://www.gutenberg.org/files/5708/5708-0.txt",   #Stray Pearls: Memoirs of Margaret De Ribaumont, Viscountess of Bellaise by Yonge
    "https://www.gutenberg.org/files/32200/32200-0.txt", #Sowing and Sewing: A Sexagesima Story by Charlotte M. Yonge
    "https://www.gutenberg.org/files/5251/5251-0.txt",   #The Long Vacation by Charlotte M. Yonge
    "https://www.gutenberg.org/files/6007/6007-0.txt",   #The Two Sides of the Shield by Charlotte M. Yonge
    "https://www.gutenberg.org/files/12449/12449-0.txt", #A Reputed Changeling; Or, Three Seventh Years Two Centuries Ago by Yonge
    "https://www.gutenberg.org/files/4236/4236-0.txt",   #Dynevor Terrace; Or, The Clue of Life — Volume 2 by Charlotte M. Yonge
    "https://www.gutenberg.org/files/9959/9959-0.txt",   #The Armourer's Prentices by Charlotte M. Yonge
    "https://www.gutenberg.org/files/4364/4364-0.txt",   #The Lances of Lynwood by Charlotte M. Yonge
    "https://www.gutenberg.org/files/3139/3139-0.txt",   #The Dove in the Eagle's Nest by Charlotte M. Yonge
    "https://www.gutenberg.org/files/4267/4267-0.txt",   #Abbeychurch; Or, Self-Control and Self-Conceit by Charlotte M. Yonge
    "https://www.gutenberg.org/files/2573/2573-0.txt",   #The Caged Lion by Charlotte M. Yonge
    "https://www.gutenberg.org/files/5156/5156-0.txt",   #Beechcroft at Rockstone by Charlotte M. Yonge
    "https://www.gutenberg.org/files/4271/4271-0.txt",   #A Modern Telemachus by Charlotte M. Yonge
    "https://www.gutenberg.org/files/5313/5313-0.txt",   #The Herd Boy and His Hermit by Charlotte M. Yonge
    "https://www.gutenberg.org/files/4296/4296-0.txt",   #Friarswood Post Office by Charlotte M. Yonge
    "https://www.gutenberg.org/files/21223/21223-0.txt", #The Carbonels by Charlotte M. Yonge
    "https://www.gutenberg.org/files/7387/7387-0.txt",   #Grisly Grisell; Or, The Laidly Lady of Whitburn: A Tale of the Wars of the…
    "https://www.gutenberg.org/files/20323/20323-0.txt", #That Stick by Charlotte M. Yonge
    "https://www.gutenberg.org/files/4659/4659-0.txt",   #Lady Hester; Or, Ursula's Narrative by Charlotte M. Yonge
    "https://www.gutenberg.org/files/9926/9926-0.txt",   #The Two Guardians by Charlotte M. Yonge
    "https://www.gutenberg.org/files/4053/4053-0.txt",   #Nuttie's Father by Charlotte M. Yonge
    "https://www.gutenberg.org/files/4944/4944-0.txt",   #Scenes and Characters, or, Eighteen Months at Beechcroft by Charlotte M. Yonge
    "https://www.gutenberg.org/files/12485/12485-0.txt", #The Three Brides by Charlotte M. Yonge
    "https://www.gutenberg.org/files/3696/3696-0.txt",   #The Prince and the Page: A Story of the Last Crusade by Charlotte M. Yonge
    "https://www.gutenberg.org/files/4347/4347-0.txt",   #My Young Alcides: A Faded Photograph by Charlotte M. Yonge
    "https://www.gutenberg.org/files/24651/24651-0.txt", #Old Times at Otterbourne by Charlotte M. Yonge
    "https://www.gutenberg.org/files/25493/25493-0.txt", #A Cathedral Courtship by Kate Douglas Smith Wiggin
    "https://www.gutenberg.org/files/721/721-0.txt",     #The Birds' Christmas Carol by Kate Douglas Smith Wiggin
    "https://www.gutenberg.org/files/18531/18531-0.txt", #Timothy's Quest by Kate Douglas Smith Wiggin
    "https://www.gutenberg.org/files/15630/15630-0.txt", #Polly Oliver's Problem by Kate Douglas Smith Wiggin
    "https://www.gutenberg.org/files/13506/13506-0.txt", #The Story of Patsy by Kate Douglas Smith Wiggin
    "https://www.gutenberg.org/files/28877/28877-0.txt", #Penelope's Progress by Kate Douglas Smith Wiggin
    "https://www.gutenberg.org/files/28006/28006-0.txt", #The Perpetual Curate by Mrs. Oliphant
    "https://www.gutenberg.org/files/10052/10052-0.txt", #The Open Door, and the Portrait. by Mrs. Oliphant
    "https://www.gutenberg.org/files/41286/41286-0.txt", #Miss Marjoribanks by Mrs. Oliphant
    "https://www.gutenberg.org/files/28629/28629-0.txt", #Phoebe, Junior by Mrs. Oliphant
    "https://www.gutenberg.org/files/48197/48197-0.txt", #Hester: A Story of Contemporary Life, Volume 1 (of 3) by Mrs. Oliphant
    "https://www.gutenberg.org/files/48199/48199-0.txt", #Hester: A Story of Contemporary Life, Volume 3 (of 3) by Mrs. Oliphant
    "https://www.gutenberg.org/files/55868/55868-0.txt", #Lady William by Mrs. Oliphant
    "https://www.gutenberg.org/files/54106/54106-0.txt", #Neighbours on the Green by Mrs. Oliphant
    "https://www.gutenberg.org/files/59918/59918-0.txt", #The Story of a Governess by Mrs. Oliphant
    "https://www.gutenberg.org/files/42045/42045-0.txt", #The Curate in Charge by Mrs. Oliphant
    "https://www.gutenberg.org/files/11521/11521-0.txt", #A Beleaguered City by Mrs. Oliphant
    "https://www.gutenberg.org/files/42013/42013-0.txt", #Salem Chapel, v. 1/2 by Mrs. Oliphant
    "https://www.gutenberg.org/files/54108/54108-0.txt", #Squire Arden; volume 1 of 3 by Mrs. Oliphant
    "https://www.gutenberg.org/files/47619/47619-0.txt", #At His Gates: A Novel. Vol. 2 (of 3) by Mrs. Oliphant
    "https://www.gutenberg.org/files/45816/45816-0.txt", #The House on the Moor, v. 1/3 by Mrs. Oliphant
    "https://www.gutenberg.org/files/63902/63902-0.txt", #The Duke's Daughter; and, The Fugitives; vol. 2/3 by Mrs. Oliphant
    "https://www.gutenberg.org/files/28637/28637-0.txt", #The Marriage of Elinor by Mrs. Oliphant
    "https://www.gutenberg.org/files/55122/55122-0.txt", #The Athelings; or, the Three Gifts. Complete by Mrs. Oliphant
    "https://www.gutenberg.org/files/51265/51265-0.txt", #The Last of the Mortimers: A Story in Two Voices by Mrs. Oliphant
    "https://www.gutenberg.org/files/53744/53744-0.txt", #Sir Robert's Fortune: A Novel by Mrs. Oliphant
    "https://www.gutenberg.org/files/71919/71919-0.txt", #Christian Melville by Mrs. Oliphant
    "https://www.gutenberg.org/files/53583/53583-0.txt", #Ombra by Mrs. Oliphant
    "https://www.gutenberg.org/files/55827/55827-0.txt", #Who Was Lost and Is Found: A Novel by Mrs. Oliphant
    "https://www.gutenberg.org/files/45818/45818-0.txt", #The House on the Moor, v. 3/3 by Mrs. Oliphant
    "https://www.gutenberg.org/files/44080/44080-0.txt", #Madonna Mary by Mrs. Oliphant
    "https://www.gutenberg.org/files/47555/47555-0.txt", #The Wizard's Son, Vol. 1 (of 3) by Mrs. Oliphant
    "https://www.gutenberg.org/files/54122/54122-0.txt", #Squire Arden; volume 2 of 3 by Mrs. Oliphant
    "https://www.gutenberg.org/files/55155/55155-0.txt", #Old Mr. Tredgold by Mrs. Oliphant
    "https://www.gutenberg.org/files/52575/52575-0.txt", #The Cuckoo in the Nest, v. 1/2 by Mrs. Oliphant
    "https://www.gutenberg.org/files/47591/47591-0.txt", #The Ladies Lindores, Vol. 1 (of 3) by Mrs. Oliphant
    "https://www.gutenberg.org/files/48198/48198-0.txt", #Hester: A Story of Contemporary Life, Volume 2 (of 3) by Mrs. Oliphant
    "https://www.gutenberg.org/files/52060/52060-0.txt", #The Sorceress (complete) by Mrs. Oliphant
    "https://www.gutenberg.org/files/63562/63562-0.txt", #Harry Joscelyn; vol. 3 of 3 by Mrs. Oliphant
    "https://www.gutenberg.org/files/65329/65329-0.txt", #Mrs. Arthur; vol. 2 of 3 by Mrs. Oliphant
    "https://www.gutenberg.org/files/65153/65153-0.txt", #Within the Precincts by Mrs. Oliphant
    "https://www.gutenberg.org/files/65328/65328-0.txt", #Mrs. Arthur; vol. 1 of 3 by Mrs. Oliphant
    "https://www.gutenberg.org/files/72221/72221-0.txt", #Carità by Mrs. Oliphant
    "https://www.gutenberg.org/files/58462/58462-0.txt", #The Story of Valentine and His Brother by Mrs. Oliphant
    "https://www.gutenberg.org/files/49597/49597-0.txt", #It was a Lover and His Lass by Mrs. Oliphant
    "https://www.gutenberg.org/files/47620/47620-0.txt", #At His Gates: A Novel. Vol. 3 (of 3) by Mrs. Oliphant
    "https://www.gutenberg.org/files/47557/47557-0.txt", #The Wizard's Son, Vol. 3 (of 3) by Mrs. Oliphant
    "https://www.gutenberg.org/files/64540/64540-0.txt", #The Greatest Heiress in England by Mrs. Oliphant
    "https://www.gutenberg.org/files/61916/61916-0.txt", #Effie Ogilvie: the story of a young life (Complete) by Mrs. Oliphant
    "https://www.gutenberg.org/files/53182/53182-0.txt", #The Sorceress, v. 3 of 3 by Mrs. Oliphant
    "https://www.gutenberg.org/files/52388/52388-0.txt", #Whiteladies by Mrs. Oliphant
    "https://www.gutenberg.org/files/10050/10050-0.txt", #A Little Pilgrim: Stories of the Seen and the Unseen by Mrs. Oliphant
    "https://www.gutenberg.org/files/65226/65226-0.txt", #John, A Love Story; vol. 1 of 2 by Mrs. Oliphant
    "https://www.gutenberg.org/files/29890/29890-0.txt", #The Doctor's Family by Mrs. Oliphant
    "https://www.gutenberg.org/files/61954/61954-0.txt", #The Lady's Walk by Mrs. Oliphant
    "https://www.gutenberg.org/files/63142/63142-0.txt", #Harry Joscelyn; vol. 1 of 3 by Mrs. Oliphant
    "https://www.gutenberg.org/files/64778/64778-0.txt", #He that will not when he may; vol. II by Mrs. Oliphant
    "https://www.gutenberg.org/files/59055/59055-0.txt", #The Heir Presumptive and the Heir Apparent by Mrs. Oliphant
    "https://www.gutenberg.org/files/54841/54841-0.txt", #Brownlows: A Novel by Mrs. Oliphant
    "https://www.gutenberg.org/files/59759/59759-0.txt", #The Executor by Mrs. Oliphant
    "https://www.gutenberg.org/files/71671/71671-0.txt", #Innocent : a tale of modern life by Mrs. Oliphant
    "https://www.gutenberg.org/files/65631/65631-0.txt", #May; vol. I by Mrs. Oliphant
    "https://www.gutenberg.org/files/65458/65458-0.txt", #The Primrose Path: A Chapter in the Annals of the Kingdom of Fife by Mrs. Oliphant
    "https://www.gutenberg.org/files/62466/62466-0.txt", #The Prodigals and Their Inheritance; Complete by Mrs. Oliphant
    "https://www.gutenberg.org/files/52756/52756-0.txt", #The Cuckoo in the Nest, v. 2/2 by Mrs. Oliphant
    "https://www.gutenberg.org/files/61445/61445-0.txt", #A House Divided Against Itself (Complete) by Mrs. Oliphant
    "https://www.gutenberg.org/files/58710/58710-0.txt", #The Land of Darkness by Mrs. Oliphant
    "https://www.gutenberg.org/files/53645/53645-0.txt", #Heart and Cross by Mrs. Oliphant
    "https://www.gutenberg.org/files/66376/66376-0.txt", #Young Musgrave by Mrs. Oliphant
    "https://www.gutenberg.org/files/63903/63903-0.txt", #The Duke's Daughter; and, The Fugitives; vol. 3/3 by Mrs. Oliphant
    "https://www.gutenberg.org/files/66376/66376-0.txt", #Sir Tom by Mrs. Oliphant
    "https://www.gutenberg.org/files/47618/47618-0.txt", #At His Gates: A Novel. Vol. 1 (of 3) by Mrs. Oliphant
    "https://www.gutenberg.org/files/74734/74734-0.txt", #Caleb Field : A tale of the Puritans by Mrs. Oliphant
    "https://www.gutenberg.org/files/61782/61782-0.txt", #A Poor Gentleman by Mrs. Oliphant
    "https://www.gutenberg.org/files/47592/47592-0.txt", #The Ladies Lindores, Vol. 2 (of 3) by Mrs. Oliphant
    "https://www.gutenberg.org/files/55784/55784-0.txt", #Two Strangers by Mrs. Oliphant
    "https://www.gutenberg.org/files/47593/47593-0.txt", #The Ladies Lindores, Vol. 3 (of 3) by Mrs. Oliphant
    "https://www.gutenberg.org/files/63158/63158-0.txt", #Harry Joscelyn; vol. 2 of 3 by Mrs. Oliphant
    "https://www.gutenberg.org/files/58707/58707-0.txt", #Kirsteen: The Story of a Scotch Family Seventy Years Ago by Mrs. Oliphant
    "https://www.gutenberg.org/files/45817/45817-0.txt", #The House on the Moor, v. 2/3 by Mrs. Oliphant
    "https://www.gutenberg.org/files/58253/58253-0.txt", #The Minister's Wife by Mrs. Oliphant
    "https://www.gutenberg.org/files/64779/64779-0.txt", #He that will not when he may; vol. III by Mrs. Oliphant
    "https://www.gutenberg.org/files/59720/59720-0.txt", #The Son of His Father; vol. 1/3 by Mrs. Oliphant
    "https://www.gutenberg.org/files/55166/55166-0.txt", #The Unjust Steward; or, The Minister's Debt by Mrs. Oliphant
    "https://www.gutenberg.org/files/52615/52615-0.txt", #The Two Marys by Mrs. Oliphant
    "https://www.gutenberg.org/files/65633/65633-0.txt", #May; vol. II by Mrs. Oliphant
    "https://www.gutenberg.org/files/55140/55140-0.txt", #A House in Bloomsbury by Mrs. Oliphant
    "https://www.gutenberg.org/files/63302/63302-0.txt", #Cousin Mary by Mrs. Oliphant
    "https://www.gutenberg.org/files/59721/59721-0.txt", #The Son of His Father; vol. 2/3 by Mrs. Oliphant
    "https://www.gutenberg.org/files/59424/59424-0.txt", #The Railway Man and His Children by Mrs. Oliphant
    "https://www.gutenberg.org/files/47556/47556-0.txt", #The Wizard's Son, Vol. 2 (of 3) by Mrs. Oliphant
    "https://www.gutenberg.org/files/61482/61482-0.txt", #The Mystery of Mrs. Blencarrow by Mrs. Oliphant
    "https://www.gutenberg.org/files/65227/65227-0.txt", #John, A Love Story; vol. 2 of 2 by Mrs. Oliphant
    "https://www.gutenberg.org/files/58323/58323-0.txt", #The Three Brothers; Complete by Mrs. Oliphant
    "https://www.gutenberg.org/files/74930/74930-0.txt", #Memoirs and resolutions of Adam Graeme of Mossgray, including some chronicles…
    "https://www.gutenberg.org/files/57988/57988-0.txt", #A son of the soil by Mrs. Oliphant
    "https://www.gutenberg.org/files/63901/63901-0.txt", #The Duke's Daughter; and, The Fugitives; vol. 1/3 by Mrs. Oliphant
    "https://www.gutenberg.org/files/64777/64777-0.txt", #He that will not when he may; vol. I by Mrs. Oliphant
    "https://www.gutenberg.org/files/10051/10051-0.txt", #The Little Pilgrim: Further Experiences. by Mrs. Oliphant
    "https://www.gutenberg.org/files/65935/65935-0.txt", #For love and life; vol. 2 of 2 by Mrs. Oliphant
    "https://www.gutenberg.org/files/15410/15410-0.txt", #A Little Pilgrim in the Unseen by Mrs. Oliphant
    "https://www.gutenberg.org/files/60018/60018-0.txt", #The Son of His Father; vol. 3/3 by Mrs. Oliphant
    "https://www.gutenberg.org/files/63582/63582-0.txt", #Oliver's Bride; A true Story by Mrs. Oliphant
    "https://www.gutenberg.org/files/59326/59326-0.txt", #The Quiet Heart by Mrs. Oliphant
    "https://www.gutenberg.org/files/65934/65934-0.txt", #For love and life; vol. 1 of 2 by Mrs. Oliphant
    "https://www.gutenberg.org/files/73086/73086-0.txt", #Harry Muir : A story of Scottish life, vol. 3 (of 3) by Mrs. Oliphant
    "https://www.gutenberg.org/files/72777/72777-0.txt", #Harry Muir : A story of Scottish life, vol. 2 (of 3) by Mrs. Oliphant
    "https://www.gutenberg.org/files/72715/72715-0.txt", #Harry Muir : A story of Scottish life, vol. 1 (of 3) by Mrs. Oliphant
    "https://www.gutenberg.org/files/78381/78381-0.txt", #An odd couple by Mrs. Oliphant
    "https://www.gutenberg.org/files/58459/58459-0.txt", #Lady Car: The Sequel of a Life by Mrs. Oliphant
    "https://www.gutenberg.org/files/58446/58446-0.txt", #Sons and Daughters by Mrs. Oliphant
    "https://www.gutenberg.org/files/29891/29891-0.txt", #The Rector by Mrs. Oliphant
    "https://www.gutenberg.org/files/24898/24898-0.txt", #Robert Elsmere by Mrs. Humphry Ward
    "https://www.gutenberg.org/files/8076/8076-0.txt",   #The History of David Grieve by Mrs. Humphry Ward
    "https://www.gutenberg.org/files/13728/13728-0.txt", #Marcella by Mrs. Humphry Ward
    "https://www.gutenberg.org/files/9633/9633-0.txt",   #Sir George Tressady — Volume I by Mrs. Humphry Ward
    "https://www.gutenberg.org/files/9634/9634-0.txt",   #Sir George Tressady — Volume II by Mrs. Humphry Ward
    "https://www.gutenberg.org/files/9441/9441-0.txt",   #Helbeck of Bannisdale — Volume I by Mrs. Humphry Ward
    "https://www.gutenberg.org/files/9442/9442-0.txt",   #Helbeck of Bannisdale — Volume II by Mrs. Humphry Ward
]
