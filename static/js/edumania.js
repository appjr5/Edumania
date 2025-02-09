// const courses = [
//     {
//         url: "#"
//         title: "Math"
//         thumbnail: ""
//         category: ""
//         description: ""
//         price:""
//         duration:""
//     },
//     {
//         url: "#"
//         title: "Math"
//         thumbnail: ""
//         category: ""
//         description: ""
//         price:""
//         duration:""
//     },
//     {
//         url: "#"
//         title: "Math"
//         thumbnail: ""
//         category: ""
//         description: ""
//         price:""
//         duration:""
//     },
//     {
//         url: "#"
//         title: "Math"
//         thumbnail: ""
//         category: ""
//         description: ""
//         price:""
//         duration:""
//     },
// ]
// const displayCourse = (urlValue, 
// titleValue, 
// categoryValue, 
// descriptionValue, 
// thumbnailValue, 
// priceValue, 
// durationValue)
// {
//     const card = document.createElementt("div");
//     card.classList.add("card");

//     const a = document.createElementt("a");
//     a.setAttribute("href", urlValue);

//     const category = document.createElementt("div");
//     category.classList.add("category");
//     category.innerHTML = categoryValue;

//     const img = document.createElementt("img");
//     img.setAttribute("src", thumbnailValue);

//     const title = document.createElementt("h2");
//     title.classList.add("title");
//     title.innerHTML = titleValue;

//     const description = document.createElementt("div");
//     description.classList.add("description");
//     description.innerHTML = descriptionValue;

//     const info = document.createElementt("div");
//     info.classList.add("info");

    
// }
            function toogleTheme() {
                const body = document.body;
                const = document.querySelector('.fa-adjust');

                body.classList.toogle("dark-theme");

                if (body.classList.contains("dark-theme")) {
                    style.color = '#f1c40f';
                }
                else {
                    style.color = '#343a40';
                }
            }
            // ---------horizontal-navbar-menu-----------
		var tabsNewAnim = $('#navbar-animmenu');
		var selectorNewAnim = $('#navbar-animmenu').find('li').length;
		//var selectorNewAnim = $(".tabs").find(".selector");
		var activeItemNewAnim = tabsNewAnim.find('.active');
		var activeWidthNewAnimWidth = activeItemNewAnim.innerWidth();
		var itemPosNewAnimLeft = activeItemNewAnim.position();
		$(".hori-selector").css({
			"left":itemPosNewAnimLeft.left + "px",
			"width": activeWidthNewAnimWidth + "px"
		});
		$("#navbar-animmenu").on("click","li",function(e){
			$('#navbar-animmenu ul li').removeClass("active");
			$(this).addClass('active');
			var activeWidthNewAnimWidth = $(this).innerWidth();
			var itemPosNewAnimLeft = $(this).position();
			$(".hori-selector").css({
				"left":itemPosNewAnimLeft.left + "px",
				"width": activeWidthNewAnimWidth + "px"
			});
		});