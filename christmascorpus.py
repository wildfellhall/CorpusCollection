"""
It's time. 

Will initially follow the same time period as all of my other lists (pre-1900).
I'm expanding the time period for this one up to the 1920s just because I would rather go slightly later in time than broaden the genre too much. 
As the Christmas genre is comparatively specific, I may expand the definition to include
wintery domestic works (ie. Little Women) and general winter-centric works. 
"""

sources = [
  "https://www.gutenberg.org/cache/epub/46/pg46.txt",       #A Christmas Carol in Prose; Being a Ghost Story of Christmas by Charles Dickens
  "https://www.gutenberg.org/cache/epub/28198/pg28198.txt", #A Budget of Christmas Tales by Charles Dickens and Others by Charles Dickens et al.
  "https://www.gutenberg.org/cache/epub/653/pg653.txt",     #The Chimes by Charles Dickens
  "https://www.gutenberg.org/cache/epub/644/pg644.txt",     #The Haunted Man and the Ghost's Bargain by Charles Dickens
  "https://www.gutenberg.org/cache/epub/721/pg721.txt",     #The Birds' Christmas Carol by Kate Douglas Smith Wiggin
  "https://www.gutenberg.org/cache/epub/10679/pg10679.txt", #The Story of the Other Wise Man by Henry Van Dyke
  "https://www.gutenberg.org/cache/epub/8694/pg8694.txt",   #The Abbot's Ghost, or Maurice Treherne's Temptation: A Christmas Story by Alcott
  "https://www.gutenberg.org/cache/epub/31103/pg31103.txt", #A Christmas Greeting: A Series of Stories by H. C. Andersen
  "https://www.gutenberg.org/cache/epub/25927/pg25927.txt", #The Christmas Story from David Harum by Edward Noyes Westcott
  "https://www.gutenberg.org/cache/epub/1415/pg1415.txt",   #Doctor Marigold by Charles Dickens
  "https://www.gutenberg.org/cache/epub/16052/pg16052.txt", #The Brownies and Other Tales by Juliana Horatia Ewing
  "https://www.gutenberg.org/cache/epub/1394/pg1394.txt",   #The Holly-Tree by Charles Dickens
  "https://www.gutenberg.org/cache/epub/47333/pg47333.txt", #Christmas Stories from French and Spanish Writers by Antoinette Ogden
  "https://www.gutenberg.org/cache/epub/58409/pg58409.txt", #Cossack Tales by Nikolai Vasilevich Gogol
  "https://www.gutenberg.org/cache/epub/28098/pg28098.txt", #Holiday Tales: Christmas in the Adirondacks by W. H. H. Murray
  "https://www.gutenberg.org/cache/epub/16134/pg16134.txt", #The First Christmas Tree: A Story of the Forest by Henry Van Dyke
  "https://www.gutenberg.org/cache/epub/20018/pg20018.txt", #Evenings at Donaldson Manor; Or, The Christmas Guest by Maria J. McIntosh
  "https://www.gutenberg.org/cache/epub/58558/pg58558.txt", #Christmas at Thompson Hall by Anthony Trollope
  "https://www.gutenberg.org/cache/epub/20251/pg20251.txt", #Christmas Comes but Once a Year by John Leighton
  "https://www.gutenberg.org/cache/epub/10723/pg10723.txt", #Betty's Bright Idea; Deacon Pitkin's Farm; and the First Christmas of New…
  "https://www.gutenberg.org/cache/epub/19608/pg19608.txt", #The Story of the Other Wise Man by Henry Van Dyke
  "https://www.gutenberg.org/cache/epub/42961/pg42961.txt", #The House With Sixty Closets: A Christmas Story for Young Folks and Old…
  "https://www.gutenberg.org/cache/epub/61193/pg61193.txt", #Mr. Pickwick's Christmas by Charles Dickens
  "https://www.gutenberg.org/cache/epub/31993/pg31993.txt", #'Round the yule-log: Christmas in Norway by Peter Christen Asbjørnsen
  "https://www.gutenberg.org/cache/epub/14624/pg14624.txt", #Santa Claus's Partner by Thomas Nelson Page
  "https://www.gutenberg.org/cache/epub/38279/pg38279.txt", #How John Norton the Trapper Kept His Christmas by W. H. H. Murray
  "https://www.gutenberg.org/cache/epub/43190/pg43190.txt", #Blade-O'-Grass. Golden Grain. and Bread and Cheese and Kisses. by B. L. Farjeon
  "https://www.gutenberg.org/cache/epub/26779/pg26779.txt", #The Ghost by William Douglas O'Connor
  "https://www.gutenberg.org/cache/epub/64152/pg64152.txt", #The Strange Visitation by Marie Corelli
  "https://www.gutenberg.org/cache/epub/44547/pg44547.txt", #Polly: A Christmas Recollection by Thomas Nelson Page
  "https://www.gutenberg.org/cache/epub/41831/pg41831.txt", #Betty Leicester's Christmas by Sarah Orne Jewett
  "https://www.gutenberg.org/cache/epub/48747/pg48747.txt", #Who Ate the Pink Sweetmeat? And Other Christmas Stories by Susan Coolidge et al.
  "https://www.gutenberg.org/cache/epub/28307/pg28307.txt", #A Christmas Accident and Other Stories by Annie Eliot Trumbull
  "https://www.gutenberg.org/cache/epub/32520/pg32520.txt", #Hildegarde's Harvest by Laura Elizabeth Howe Richards
  "https://www.gutenberg.org/cache/epub/34665/pg34665.txt", #Christmas Penny Readings: Original Sketches for the Season by George Manville Fenn
  "https://www.gutenberg.org/cache/epub/14534/pg14534.txt", #Christmas with Grandma Elsie by Martha Finley
  "https://www.gutenberg.org/cache/epub/70198/pg70198.txt", #Seven Xmas Eves : Being the romance of a social evolution by Richard Dehan et al.
  "https://www.gutenberg.org/cache/epub/23063/pg23063.txt", #The Lost Child by François Coppée
  "https://www.gutenberg.org/cache/epub/4384/pg4384.txt",   #The Lost Word: A Christmas Legend of Long Ago by Henry Van Dyke
  "https://www.gutenberg.org/cache/epub/56410/pg56410.txt", #Ruby: A Story of the Australian Bush by Molly E. Jamieson
  "https://www.gutenberg.org/cache/epub/74849/pg74849.txt", #The Christmas earnings : Or, Ethel Fletcher's temptation by Lucy Ellen Guernsey
  "https://www.gutenberg.org/cache/epub/3719/pg3719.txt",   #The Mistletoe Bough by Anthony Trollope
  "https://www.gutenberg.org/cache/epub/72586/pg72586.txt", #Ginevra : or, The old oak chest, a Christmas story by Susan E. Wallace
  "https://www.gutenberg.org/cache/epub/20200/pg20200.txt", #Christmas, A Happy Time by Alicia Catherine Mant
  "https://www.gutenberg.org/cache/epub/20180/pg20180.txt", #Mr. Kris Kringle: A Christmas Tale by S. Weir Mitchell
  "https://www.gutenberg.org/cache/epub/56599/pg56599.txt", #The Fortunes of the Colville Family; or, A Cloud with its Silver Lining by Smedley
  "https://www.gutenberg.org/cache/epub/55281/pg55281.txt", #The Christmas Dream of Little Charles by Redfield, Justus Starr
  "https://www.gutenberg.org/cache/epub/77220/pg77220.txt", #Tabby's travels : or the holiday adventures of a kitten by Lucy Ellen Guernsey
  "https://www.gutenberg.org/cache/epub/53920/pg53920.txt", #Kittyboy's Christmas by Amy Ella Blanchard
  "https://www.gutenberg.org/cache/epub/64117/pg64117.txt", #The Christmas Holly by Marion Harland
  "https://www.gutenberg.org/cache/epub/75031/pg75031.txt", #Corrie by active approximately 1876-1880 Ruth Lynn
  "https://www.gutenberg.org/cache/epub/22665/pg22665.txt", #Christian Gellert's Last Christmas by Berthold Auerbach
  "https://www.gutenberg.org/cache/epub/74860/pg74860.txt", #Elsie : a Christmas story by Alexander Lange Kielland
  "https://www.gutenberg.org/cache/epub/64094/pg64094.txt", #Christmas on Wheels by Willis Boyd Allen
  "https://www.gutenberg.org/cache/epub/5591/pg5591.txt",   #The Nuts: A Christmas Story for my Children and Grandchildren by Georg Ebers
  "https://www.gutenberg.org/cache/epub/35397/pg35397.txt", #Christmas Stories by Edward Berens
  "https://www.gutenberg.org/cache/epub/67194/pg67194.txt", #Christmas Holidays; or, a Visit at Home by Anonymous
  "https://www.gutenberg.org/cache/epub/71698/pg71698.txt", #Christmas at Cedar Hill : A holiday story-book by Lucy Ellen Guernsey
  "https://www.gutenberg.org/cache/epub/79517/pg79517.txt", #Christie's Christmas by Pansy
  "https://www.gutenberg.org/cache/epub/65830/pg65830.txt", #Two Christmas Stories: Sam Franklin's Savings-Bank; A Miserable Christmas and…
  "https://www.gutenberg.org/cache/epub/72610/pg72610.txt", #The Christmas gift : A story for little folks by Oliver Optic
  "https://www.gutenberg.org/cache/epub/70279/pg70279.txt", #Bertha Weisser's wish : A Christmas story by Mary L. Bissell
  "https://www.gutenberg.org/cache/epub/70291/pg70291.txt", #X-mas sketches from the Dartmouth Literary Monthly by Edwin Osgood Grover
  "https://www.gutenberg.org/cache/epub/68424/pg68424.txt", #Magic words: A tale for Christmas time by Emilie Maceroni
  "https://www.gutenberg.org/cache/epub/72621/pg72621.txt", #Our Christmas party by Edwin Hodder
  "https://www.gutenberg.org/cache/epub/1467/pg1467.txt",   #Some Christmas Stories by Charles Dickens
  "https://www.gutenberg.org/cache/epub/809/pg809.txt",     #Holiday Romance by Charles Dickens
  "https://www.gutenberg.org/cache/epub/678/pg678.txt",     #The Cricket on the Hearth: A Fairy Tale of Home by Charles Dickens
  "https://www.gutenberg.org/cache/epub/23540/pg23540.txt", #The Twin Cousins by Sophie May
  "https://www.gutenberg.org/cache/epub/52935/pg52935.txt", #Mr. Blake's Walking-Stick: A Christmas Story for Boys and Girls by Edward Eggleston
  "https://www.gutenberg.org/cache/epub/40269/pg40269.txt", #At the Black Rocks by Edward A. Rand
  "https://www.gutenberg.org/cache/epub/26015/pg26015.txt", #A Christmas Posy by Mrs. Molesworth
  "https://www.gutenberg.org/cache/epub/14202/pg14202.txt", #Little Prudy's Sister Susy by Sophie May
  "https://www.gutenberg.org/cache/epub/45666/pg45666.txt", #Little Peter: A Christmas Morality for Children of any Age by Lucas Malet
  "https://www.gutenberg.org/cache/epub/38564/pg38564.txt", #Happy Hearts by June Isle
  "https://www.gutenberg.org/cache/epub/20425/pg20425.txt", #The Peace Egg and Other tales by Juliana Horatia Ewing
  "https://www.gutenberg.org/cache/epub/48325/pg48325.txt", #Karl Krinken, His Christmas Stocking by Susan Warner and Anna Bartlett Warner
  "https://www.gutenberg.org/cache/epub/39210/pg39210.txt", #The Ice Queen by Ernest Ingersoll
  "https://www.gutenberg.org/cache/epub/36431/pg36431.txt", #The Palace in the Garden by Mrs. Molesworth
  "https://www.gutenberg.org/cache/epub/34045/pg34045.txt", #A Christmas Child: A Sketch of a Boy-Life by Mrs. Molesworth
  "https://www.gutenberg.org/cache/epub/43763/pg43763.txt", #Snap-Dragons; Old Father Christmas by Juliana Horatia Ewing
  "https://www.gutenberg.org/cache/epub/69782/pg69782.txt", #A Southern Cross fairy tale by Kate McCosh Clark
  "https://www.gutenberg.org/cache/epub/58762/pg58762.txt", #The New-Year's Bargain by Susan Coolidge
  "https://www.gutenberg.org/cache/epub/47897/pg47897.txt", #The yule log : a series of stories for the young by Georgianna M. Bishop
  "https://www.gutenberg.org/cache/epub/71907/pg71907.txt", #Arthur Glyn : and other stories by Ruth Lamb
  "https://www.gutenberg.org/cache/epub/57413/pg57413.txt", #Down the Snow Stairs; Or, From Good-Night to Good-Morning by Alice Corkran
  "https://www.gutenberg.org/cache/epub/13379/pg13379.txt", #The Two Elsies by Martha Finley
  "https://www.gutenberg.org/cache/epub/54803/pg54803.txt", #Playing Santa Claus, and Other Christmas Tales by Sarah P. Doughty
  "https://www.gutenberg.org/cache/epub/2731/pg2731.txt",   #The Christmas Books of Mr. M.A. Titmarsh by William Makepeace Thackeray
  "https://www.gutenberg.org/cache/epub/40723/pg40723.txt", #The Battle of Life: A Love Story by Charles Dickens
  "https://www.gutenberg.org/cache/epub/1392/pg1392.txt",   #The Seven Poor Travellers by Charles Dickens
  "https://www.gutenberg.org/cache/epub/79846/pg79846.txt", #The written leaves : A story of the new year and other holiday stories
  ##### Less Strict Time Period Adherence (1900-1920) #####
  "https://www.gutenberg.org/cache/epub/64103/pg64103.txt", #Little Paulina: Christmas in Russia by Mary Cowden Clarke
  "https://www.gutenberg.org/cache/epub/70097/pg70097.txt", #A new note in the Christmas Carol by Clara Wood Mingins
  "https://www.gutenberg.org/cache/epub/70521/pg70521.txt", #The hermit's Christmas by David De Forest Burrell
  "https://www.gutenberg.org/cache/epub/72453/pg72453.txt", #The Squire's young folk : A Christmas story by Eleanora H. Stooke
  "https://www.gutenberg.org/cache/epub/78374/pg78374.txt", #Little Merry Christmas by Winifred Arnold
  "https://www.gutenberg.org/cache/epub/70294/pg70294.txt", #The First Church's Christmas barrel by Caroline Abbot Stanley
  "https://www.gutenberg.org/cache/epub/67255/pg67255.txt", #The Story of Zephyr: A Christmas Story by Jeanie Oliver Davidson Smith
  "https://www.gutenberg.org/cache/epub/70273/pg70273.txt", #The boy who brought Christmas by Alice Morgan
  "https://www.gutenberg.org/cache/epub/67034/pg67034.txt", #The Child and the Dream: A Christmas Story by Marion Cook Stow
  "https://www.gutenberg.org/cache/epub/69685/pg69685.txt", #Just sweethearts: A Christmas love story by Harry Stillwell Edwards
  "https://www.gutenberg.org/cache/epub/69068/pg69068.txt", #The country Christmas by Frances Margaret Fox
  "https://www.gutenberg.org/cache/epub/12881/pg12881.txt", #Mrs. Budlong's Christmas Presents by Rupert Hughes
  "https://www.gutenberg.org/cache/epub/74537/pg74537.txt", #The wonderful Christmas in Pumpkin Delight Lane by Sarah J. Prichard
  "https://www.gutenberg.org/cache/epub/15826/pg15826.txt", #Uncle Noah's Christmas Inspiration by Leona Dalrymple
  "https://www.gutenberg.org/cache/epub/17510/pg17510.txt", #When the Yule Log Burns: A Christmas Story by Leona Dalrymple
  "https://www.gutenberg.org/cache/epub/28110/pg28110.txt", #Jimsy: The Christmas Kid by Leona Dalrymple
  "https://www.gutenberg.org/cache/epub/45103/pg45103.txt", #In the Heart of the Christmas Pines by Leona Dalrymple
  "https://www.gutenberg.org/cache/epub/69854/pg69854.txt", #The Christmas Makers' Club by Edith A. Sawyer
  "https://www.gutenberg.org/cache/epub/15936/pg15936.txt", #The Sad Shepherd: A Christmas Story by Henry Van Dyke
  "https://www.gutenberg.org/cache/epub/704/pg704.txt",     #The Mansion by Henry Van Dyke
  "https://www.gutenberg.org/cache/epub/14946/pg14946.txt", #The Blossoming Rod by Mary Stewart Cutting
  "https://www.gutenberg.org/cache/epub/71547/pg71547.txt", #A journey in search of Christmas by Owen Wister
  "https://www.gutenberg.org/cache/epub/68590/pg68590.txt", #The Christmas Bishop by Winifred Margaretta Kirkland
  "https://www.gutenberg.org/cache/epub/71029/pg71029.txt", #Jasper's old shed, and how the light shone in by A. M. Coker
  "https://www.gutenberg.org/cache/epub/23278/pg23278.txt", #Janice Day at Poketown by Helen Beecher Long
  "https://www.gutenberg.org/cache/epub/59594/pg59594.txt", #Betty's Virginia Christmas by Molly Elliot Seawell
  "https://www.gutenberg.org/cache/epub/75689/pg75689.txt", #Beth's wonder-winter : A story by Marion Ames Taggart
  "https://www.gutenberg.org/cache/epub/30907/pg30907.txt", #Rosemary in Search of a Father by C. N. Williamson and A. M. Williamson
  "https://www.gutenberg.org/cache/epub/39753/pg39753.txt", #The Misfit Christmas Puddings by Consolation Club
  "https://www.gutenberg.org/cache/epub/27697/pg27697.txt", #The Mouse and The Moonbeam by Eugene Field
  "https://www.gutenberg.org/cache/epub/19384/pg19384.txt", #On Christmas Day In The Evening by Grace S. Richmond
  "https://www.gutenberg.org/cache/epub/53402/pg53402.txt", #Brotherly House by Grace S. Richmond
  "https://www.gutenberg.org/cache/epub/20187/pg20187.txt", #On Christmas Day in the Morning by Grace S. Richmond
  "https://www.gutenberg.org/cache/epub/67105/pg67105.txt", #The Animals' Christmas Tree by John P. Peters
  "https://www.gutenberg.org/cache/epub/64107/pg64107.txt", #Christmas in Sweden; or, A festival of light by Sarah Gertrude Pomeroy
  "https://www.gutenberg.org/cache/epub/33666/pg33666.txt", #A Captured Santa Claus by Thomas Nelson Page
  "https://www.gutenberg.org/cache/epub/25896/pg25896.txt", #Tommy Trot's Visit to Santa Claus by Thomas Nelson Page
  "https://www.gutenberg.org/cache/epub/23511/pg23511.txt", #The Christmas Peace by Thomas Nelson Page
  "https://www.gutenberg.org/cache/epub/69416/pg69416.txt", #Christmas stories by Georgene Faulkner
  "https://www.gutenberg.org/cache/epub/5303/pg5303.txt",   #The Little Hunchback Zia by Frances Hodgson Burnett
  "https://www.gutenberg.org/cache/epub/479/pg479.txt",     #Little Lord Fauntleroy by Frances Hodgson Burnett
  "https://www.gutenberg.org/cache/epub/460/pg460.txt",     #The Dawn of a To-morrow by Frances Hodgson Burnett
  "https://www.gutenberg.org/cache/epub/38555/pg38555.txt", #Dorothy Dale in the City by Margaret Penrose
  "https://www.gutenberg.org/cache/epub/37152/pg37152.txt", #A Maid of Many Moods by Virna Sheard
  "https://www.gutenberg.org/cache/epub/5949/pg5949.txt",   #Beasley's Christmas Party by Booth Tarkington
  "https://www.gutenberg.org/cache/epub/14723/pg14723.txt", #How It Happened by Kate Langley Bosher
  "https://www.gutenberg.org/cache/epub/12971/pg12971.txt", #The Man in Lonely Land by Kate Langley Bosher
  "https://www.gutenberg.org/cache/epub/44796/pg44796.txt", #The Prodigal Village: A Christmas Tale by Irving Bacheller
]
