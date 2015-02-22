
module.exports = function(grunt) {
    
    var path = 'dev/script/';
	var sourceFiles = [];

	//config
	grunt.initConfig({
		pkg : grunt.file.readJSON('package.json'),
		sass : {
			dist : {
				options: {                       // Target options
					style: 'compact'				},
				files : {
					'app/css/main.css' : 'dev/styles/main.scss'
				}
			}
		},
		concat: {
			options : {
				stripBanners : true,
				banner : '/*! <%= pkg.name %> - v<%= pkg.version %> - ' +
					'<%= grunt.template.today("yyyy-mm-dd") %> */',
				separator : '\n\n'
			},
			dist : {
				src : sourceFiles,
				dest : 'dev/srcipt/script.js'
			}
		},
		uglify: {
            my_target: {
                files: {
                'app/script.min.js': '<%= concat.dist.dest %>'
                }
            }
		}
//        ,
//        'ftp-deploy' : {
//            build : {
//                auth : {
//                    host : 'ftp.anthonyladson.com',
//                    port : 21,
//                    authKey : "key1"
//                },
//                src : 'game',
//                dest : 'quintessence',
//                exclusions : ['.*']
//            }
//        }
	});

	//load task
	grunt.loadNpmTasks('grunt-contrib-sass');
	grunt.loadNpmTasks('grunt-contrib-concat');
	grunt.loadNpmTasks('grunt-contrib-uglify');
//	grunt.loadNpmTasks('grunt-ftp-deploy');

	//register task
	grunt.registerTask('default', ['sass','concat','uglify']);
	grunt.registerTask('css',['sass']);
//	grunt.registerTask('deploy',['default','ftp-deploy']);

};