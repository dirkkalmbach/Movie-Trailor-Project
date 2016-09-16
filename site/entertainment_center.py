import media
import fresh_tomatoes

pointbreak = media.Movie("Pointbreak",
						"""Point Break is a 1991 American action crime thriller film directed by Kathryn Bigelow, starring Patrick Swayze, Keanu Reeves, Lori Petty and Gary Busey. 
						The title refers to the surfing term "point break," where a wave breaks as it hits a point of land jutting out from the coastline. 
						Reeves stars as rookie FBI agent Johnny Utah, who is investigating a string of bank robberies possibly being committed by surfers. 
						Johnny goes undercover to infiltrate the surfing community and develops a complex friendship with Bodhi (Swayze), the charismatic leader of a gang of surfers.""",
						"https://upload.wikimedia.org/wikipedia/en/thumb/7/7e/Pointbreaktheatrical.jpg/220px-Pointbreaktheatrical.jpg",
						"https://www.youtube.com/watch?v=AVk3mR2UhgI")

u_turn = media.Movie("U Turn",
						"""U Turn is a 1997 modern western neo-noir crime thriller film directed by Oliver Stone, and based on the book Stray Dogs by John Ridley. 
						It stars Sean Penn, Billy Bob Thornton, Jennifer Lopez, Jon Voight, Powers Boothe, Joaquin Phoenix, Claire Danes and Nick Nolte.""",
						"https://upload.wikimedia.org/wikipedia/en/thumb/0/03/U-Turnposter.jpg/220px-U-Turnposter.jpg",
						"https://www.youtube.com/watch?v=-q7tkR4Kr6c")

true_romance = media.Movie("True Romance",
							"""True Romance is a 1993 American crime film with elements of black comedy and romance, directed by Tony Scott and written by Quentin Tarantino. 
							The film stars Christian Slater and Patricia Arquette with a supporting cast featuring Dennis Hopper, Val Kilmer, Gary Oldman, Brad Pitt, and Christopher Walken.""",
							"https://upload.wikimedia.org/wikipedia/en/d/d6/True_romance.jpg",
							"https://www.youtube.com/watch?v=_wNYNDzKpuQ")


men_at_work = media.Movie("Men at Work",
							"""Men at Work is a 1990 American black comedy film written and directed by Emilio Estevez, who also starred in the lead role. 
							The film co-stars Charlie Sheen, Leslie Hope and Keith David. The film was released in the United States on August 24, 1990.""",
							"https://upload.wikimedia.org/wikipedia/en/thumb/4/43/Men_at_work_ver2.jpg/220px-Men_at_work_ver2.jpg",
							"https://www.youtube.com/watch?v=ByUyXPA8SOA")

the_boys_next_door = media.Movie("The Boys next Door",
								"The Boys Next Door is a 1985 independent adventure-crime drama film about two boys who leave their small town home on the day of their high school graduation and embark on a crime and murder spree.",
								"https://upload.wikimedia.org/wikipedia/en/thumb/8/83/Boys-next-door.jpg/215px-Boys-next-door.jpg",
								"https://www.youtube.com/watch?v=vno5JCCDKIA")

meet_the_fockers = media.Movie("Meet the Fockers",
								"""Meet the Fockers is a 2004 American comedy film directed by Jay Roach and the sequel to Meet the Parents. The film stars Robert De Niro (who was also one of the film's producers), 
								Ben Stiller, Dustin Hoffman, Barbra Streisand, Blythe Danner and Teri Polo.""",
								"https://upload.wikimedia.org/wikipedia/en/thumb/2/27/Meet_The_Fockers.jpg/220px-Meet_The_Fockers.jpg",
								"https://www.youtube.com/watch?v=JG5NnOIKeew")
movies = [pointbreak, u_turn, true_romance, men_at_work, the_boys_next_door, meet_the_fockers]

fresh_tomatoes.open_movies_page(movies)