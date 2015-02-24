
module.exports = function(grunt) {
    
    var path = 'dev/scripts/';
	var sourceFiles = ['main.js'];

	//config
	grunt.initConfig({
		pkg : grunt.file.readJSON('package.json'),
		sass : {
			dist : {
				options: {                       // Target options
					style: 'compact'				},
				files : {
					'app/css/main.css' : 'dev/styles/main.scss',
                    'app/css/maps.css' : 'dev/styles/maps.scss',
                    'app/css/contribute.css' : 'dev/styles/contribute.scss'
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
				dest : 'dev/script/script.js'
			}
		},
		uglify: {
            my_target: {
                files: {
                'app/script.min.js': '<%= concat.dist.dest %>'
                }
            }
		},
        copy: {
          main: {
            expand: true,
            cwd: 'dev/scripts/',
            src: ['**'], 
            dest: 'app/scripts/',
          }
        }
	});

	//load task
	grunt.loadNpmTasks('grunt-contrib-sass');
	grunt.loadNpmTasks('grunt-contrib-concat');
	grunt.loadNpmTasks('grunt-contrib-uglify');
    grunt.loadNpmTasks('grunt-contrib-copy');

	//register task
	grunt.registerTask('css',['sass']);
	grunt.registerTask('dev',['css','copy']);

};