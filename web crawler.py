# User Libraries
import website_manager as wm
import file_manager as fm


def stats()-> None:
	all_links = fm.get("_all_links")
	print("Total of ", len(all_links.keys()), " tags: ", all_links.keys())
	total_urls = 0
	for tag in all_links.keys():
		total_urls = total_urls + len(all_links[tag])
		print("For ", tag, ", there are ", len(all_links[tag]), " urls in data block.")
	print("There are total of ", total_urls, " posts in the data block.")

if __name__ == '__main__':
	feed_link = "https://hashnode.com/n/"
	tags = [
		# Comment out for safety and sanity while debugging.
		"javascript",
		"python",
		"github",
		"cpp"
	]

	# Links to blog posts (also used in file naming)
	all_links = {}
	data_block = {}
	for tag in tags:
		# Get urls and save them locally
		urls = wm.get_url_list(feed_link + tag)
		fm.save("tag_" + tag + "_links", data= urls)

		# Get raw text from each url and process it into tokens
		for url in urls:
			print("Processing ", fm.clean_up_name(url))
			raw = wm.get_text_from_url(url)
			# fm.save("raw_" + url, data= raw) # Optional.
			data_block[fm.clean_up_name(url)] = {
				"tag": tag,
				"raw": raw
			}

		# Update link list
		all_links[tag] = urls

	# Save the list of links and data block
	if len(all_links) > 0 and len(data_block.keys()) > 0:
		fm.save("_all_links", data= all_links)
		fm.save("_data_block", data= data_block)

	stats()


