"""
Work in progress

Note: as I continue to collate this corpus, I will attempt to blend satirical essays/shorter works with satirical novels.

Not exclusive to works originally published in English. 
"""
sources = [
  "https://www.gutenberg.org/files/1080/1080-0.txt",   # A Modest Proposal by Jonathan Swift
  "https://www.gutenberg.org/files/829/829-0.txt",     # Gulliver's Travels into Several Remote Nations of the World by Jonathan Swift
  "https://www.gutenberg.org/files/4737/4737-0.txt",   # A Tale of a Tub by Jonathan Swift
  "https://www.gutenberg.org/files/1090/1090-0.txt",   # The Bickerstaff-Partridge Papers by Jonathan Swift
  "https://www.gutenberg.org/files/121/121-0.txt",     # Northanger Abbey by Jane Austen
  "https://www.gutenberg.org/files/86/86-0.txt",       # A Connecticut Yankee in King Arthur's Court by Mark Twain
  "https://www.gutenberg.org/files/599/599-0.txt",     # Vanity Fair by William Makepeace Thackeray
  "https://www.gutenberg.org/files/3178/3178-0.txt",   # The Gilded Age: A Tale of Today by Mark Twain and Charles Dudley Warner
  "https://www.gutenberg.org/files/883/883-0.txt",     # Our Mutual Friend by Charles Dickens
  "https://www.gutenberg.org/files/1906/1906-0.txt",   # Erewhon; Or, Over the Range by Samuel Butler
  "https://www.gutenberg.org/files/4558/4558-0.txt",   # Barry Lyndon by William Makepeace Thackeray
  "https://www.gutenberg.org/files/897/897-0.txt",     # The Rose and the Ring by William Makepeace Thackeray
  "https://www.gutenberg.org/files/2686/2686-0.txt",   # The Book of Snobs by William Makepeace Thackeray
  "https://www.gutenberg.org/files/2675/2675-0.txt",   # Burlesques by William Makepeace Thackeray
  "https://www.gutenberg.org/files/2731/2731-0.txt",   # The Christmas Books of Mr. M.A. Titmarsh by William Makepeace Thackeray
  "https://www.gutenberg.org/files/2844/2844-0.txt",   # The Fatal Boots by William Makepeace Thackeray
  "https://www.gutenberg.org/files/2823/2823-0.txt",   # The Fitz-Boodle Papers by William Makepeace Thackeray
  "https://www.gutenberg.org/files/2796/2796-0.txt",   # The Memoirs of Mr. Charles J. Yellowplush by William Makepeace Thackeray
  "https://www.gutenberg.org/files/1935/1935-0.txt",   # The Tremendous Adventures of Major Gahagan by William Makepeace Thackeray
  "https://www.gutenberg.org/files/2859/2859-0.txt",   # A Little Dinner at Timmins's by William Makepeace Thackeray
  "https://www.gutenberg.org/files/61072/61072-0.txt", # "Our Street" by William Makepeace Thackeray
  "https://www.gutenberg.org/files/20001/20001-0.txt", # The English spy : an original work characteristic, satirical, and humorous.…
  "https://www.gutenberg.org/files/19942/19942-0.txt", # Candide by Voltaire
  "https://www.gutenberg.org/files/1081/1081-0.txt",   # Dead Souls by Nikolai Vasilevich Gogol
  "https://www.gutenberg.org/files/45858/45858-0.txt", # Lucian's True History by of Samosata Lucian
  "https://www.gutenberg.org/files/10430/10430-0.txt", # Trips to the Moon by of Samosata Lucian
  "https://www.gutenberg.org/files/968/968-0.txt",     # Martin Chuzzlewit by Charles Dickens
  "https://www.gutenberg.org/files/652/652-0.txt",     # Rasselas, Prince of Abyssinia by Samuel Johnson
  "https://www.gutenberg.org/files/44520/44520-0.txt", # Pamphlets and Parodies on Political Subjects by William Hone
  "https://www.gutenberg.org/files/5231/5231-0.txt",   # The Way We Live Now by Anthony Trollope
  "https://www.gutenberg.org/files/619/619-0.txt",     # The Warden by Anthony Trollope
  "https://www.gutenberg.org/files/7381/7381-0.txt",   # The Eustace Diamonds by Anthony Trollope
  "https://www.gutenberg.org/files/27533/27533-0.txt", # The Struggles of Brown, Jones, and Robinson by Anthony Trollope
  "https://www.gutenberg.org/files/21816/21816-0.txt", # The Confidence-Man: His Masquerade by Herman Melville
  "https://www.gutenberg.org/files/6053/6053-0.txt",   # Evelina, Or, the History of a Young Lady's Entrance into the World by Fanny Burney
  "https://www.gutenberg.org/files/1051/1051-0.txt",   # Sartor Resartus: The Life and Opinions of Herr Teufelsdröckh by Thomas Carlyle
  "https://www.gutenberg.org/files/3190/3190-0.txt",   # 1601: Conversation as it was by the Social Fireside in the Time of the Tudors
  "https://www.gutenberg.org/files/3172/3172-0.txt",   # Fenimore Cooper's Literary Offences by Mark Twain
  "https://www.gutenberg.org/files/21822/21822-0.txt", # A Lecture On Heads by George Alexander Stevens
  "https://www.gutenberg.org/files/10095/10095-0.txt", # The Twilight of the Gods, and Other Tales by Richard Garnett
  "https://www.gutenberg.org/files/6758/6758-0.txt",   # The Adventures of Sir Launcelot Greaves by T. Smollett
  "https://www.gutenberg.org/files/6761/6761-0.txt",   # The Adventures of Ferdinand Count Fathom — Complete by T. Smollett
  "https://www.gutenberg.org/files/4092/4092-0.txt",   # The Monikins by James Fenimore Cooper
  "https://www.gutenberg.org/files/2329/2329-0.txt",   # Autobiography of a Pocket-Handkerchief by James Fenimore Cooper
  "https://www.gutenberg.org/files/2615/2615-0.txt",   # Discourses on Satire and on Epic Poetry by John Dryden
  "https://www.gutenberg.org/files/1473/1473-0.txt",   # The Absentee by Maria Edgeworth
  "https://www.gutenberg.org/files/21337/21337-0.txt", # 'That Very Mab' by May Kendall and Andrew Lang
  "https://www.gutenberg.org/files/38411/38411-0.txt", # Froth: A Novel by Armando Palacio Valdés
  "https://www.gutenberg.org/files/9909/9909-0.txt",   # Nightmare Abbey by Thomas Love Peacock
  "https://www.gutenberg.org/files/2075/2075-0.txt",   # Crotchet Castle by Thomas Love Peacock
  "https://www.gutenberg.org/files/1079/1079-0.txt",   # The life and opinions of Tristram Shandy, gentleman by Laurence Sterne
  "https://www.gutenberg.org/files/804/804-0.txt",     # A Sentimental Journey Through France and Italy by Laurence Sterne
  "https://www.gutenberg.org/files/20257/20257-0.txt", # A Political Romance by Laurence Sterne
  "https://www.gutenberg.org/files/58070/58070-0.txt", # Home Life in Russia, Volumes 1 and 2 by Nikolai Vasilevich Gogol
  "https://www.gutenberg.org/files/46621/46621-0.txt", # Sheppard Lee, Written by Himself. Vol. 1 (of 2) by Robert Montgomery Bird
  "https://www.gutenberg.org/files/46622/46622-0.txt", # Sheppard Lee, Written by Himself. Vol. 2 (of 2) by Robert Montgomery Bird
  "https://www.gutenberg.org/files/12793/12793-0.txt", # Cobwebs from an Empty Skull by Ambrose Bierce
  "https://www.gutenberg.org/files/4793/4793-0.txt",   # The Fiend's Delight by Ambrose Bierce
  "https://www.gutenberg.org/files/55035/55035-0.txt", # The Marvellous Adventures and Rare Conceits of Master Tyll Owlglass by Mackenzie et al.
  "https://www.gutenberg.org/files/67888/67888-0.txt", # Anticipation by Richard Tickell
  "https://www.gutenberg.org/files/39726/39726-0.txt", # The Rolliad, in Two Parts by Tickell, Ellis, Laurence, and Richardson
  "https://www.gutenberg.org/files/46467/46467-0.txt", # The Remarkable History of Sir Thomas Upmore, bart., M.P., formerly known as…
  "https://www.gutenberg.org/files/3191/3191-0.txt",   # Goldsmith's Friend Abroad Again by Mark Twain
  "https://www.gutenberg.org/files/19484/19484-0.txt", # Editorial Wild Oats by Mark Twain
  "https://www.gutenberg.org/files/60900/60900-0.txt", # Merry Tales by Mark Twain
  "https://www.gutenberg.org/files/30343/30343-0.txt", # A discourse concerning ridicule and irony in writing (1729) by Anthony Collins
  "https://www.gutenberg.org/files/41950/41950-0.txt", # The Visions of Quevedo by Francisco de Quevedo
  "https://www.gutenberg.org/files/46125/46125-0.txt", # Pablo de Segovia, the Spanish Sharper by Francisco de Quevedo
  "https://www.gutenberg.org/files/75943/75943-0.txt", # Melincourt : or, Sir Oran Haut-Ton by Thomas Love Peacock
]
